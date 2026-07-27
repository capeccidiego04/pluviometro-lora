import json
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LettorePluviometro')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        uplink_message = body.get('uplink_message', {})
        decoded = uplink_message.get('decoded_payload')

        if not decoded or decoded.get('key') != 'humm' or (decoded.get('status') != 16 and decoded.get('status') != 18):
            print("Pacchetto scartato: Messaggio tecnico o chiave errata.")
            return {
                'statusCode': 200, # Rispondiamo 200 per non far riprovare TTN
                'body': json.dumps('Messaggio non applicativo ignorato')
            }

        device_id = body['end_device_ids']['device_id']
        timestamp = body['received_at']

        rain_total = float(decoded.get('rain_mm') or 0)

        battery_hex = str(decoded.get('battery_hex') or 0)

        response = table.query(
            KeyConditionExpression=Key('dev_id').eq(device_id),
            ScanIndexForward=False,
            Limit=1
        )

        items = response.get('Items', [])

        if items:
            rain_total_vecchio = float(items[0]['rain_total'])
            rain_new = rain_total_vecchio + rain_total
        else:
            rain_new = rain_total
    
        table.put_item(
                Item={
                    'dev_id': device_id,
                    'timestamp': timestamp,
                    'rain_total': str(round(rain_new, 2)),
                    'rain_delta': str(round(rain_total, 2)),
                    'battery_hex': str(battery_hex),
                    'processed_at': str(datetime.now())
                }
            )
        return {
            'statusCode': 200,
            'body': json.dumps('Dato salvato con successo!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Errore interno: {str(e)}")
        }
