# pluviometro-lora
> Architettura di un sistema di monitoraggio pluviometrico IoT su protocollo LoRaWan e Architettura Serverless AWS

1) Introduzione
2) Architettura del sistema
3) Sfide tecniche
4) Risultati?

## Introduzione
Il sistema descrive l'implementazione di una pipeline dati completa, dal rilevamento fisico delle precipitazioni alla persistenza dei dati elaborati
| Componente | Tecnologia/Modello | Ruolo |
| :--- | :--- | :--- |
| **Sensore** | Davis Instruments | Rilevazione millimetrica delle precipitazioni |
| **Nodo LoRa** | HummBox GreenCityZen | Trasmissione dati a lungo raggio |
| **Network Server** | The Things Network (TTN) | Decodifica dei pacchetti e instradamento |
| **Cloud Gateway** | AWS API Gateway | Endpoint per integrazione del WebHook |
| **Calcolo** | AWS Lambda | Elaborazione dei dati |
| **Database** | AWS DynamoDB | Archiviazione NoSQL scalabile |

## Specifiche tecniche dei componenti

### Sensore Pluviometrico

### HummBox

### TTN

### AWS API Gateway

### AWS Lambda

### Database

## Flusso dei dati
```mermaid
sequenceDiagram
  autonumber
  participant S as Sensore Pluviometrico
  participant H as HummBox
  participant T as The Things Network
  participant AWS as AWS (API/Lambda)
  participant DB as DynamoDB

  Note over S, H: Livello Fisico
    S->>H: Impulso elettrico (0.254mm)
    H->>H: Aggregazione dati

  Note over H, T: Livello Network
    H->>+T: Uplink LoRaWAN (RF)
    
  Note over T, AWS: Cloud Ingestion
  T->>-AWS: Webhook JSON (HTTPS)

  activate AWS
  AWS->>AWS: Decoding & Parsing
  AWS->>+DB: PutItem (Persistenza)
  DB-->>-AWS: 200 OK
  deactivate AWS

  Note right of DB: Dato pronto per Dashboard
```
