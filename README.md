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

### The Things Network
The Things Network è il portale che si occupa di ricevere, interpretare ed inoltrare i pacchetti

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
## Architettura del sistema
### Sensore Pluviometrico

### HummBox

### The Things Network (TTN)
The Things Network è il portale che si occupa di ricevere, interpretare ed inoltrare i pacchetti.
Dopo essersi registrati è stata creata l'applicazione "Sensore Pluviometrico" ed è stato registrato l'end device.

Per la registrazione dell'end device è necessario impostare i seguenti parametri:

| Parametro | Struttura | Significato |
| :--- | :--- | :--- |
| **App EUI** | 8 byte esadecimali | Identifica in modo univoco l'applicazione |
| **Dev EUI** | 8 byte esadecimali | Identifica in modo univoco l'end device |
| **App Key** | 16 byte esadecimali | Chiave di sicurezza per crittografare i dati durante la trasmissione |

Così facendo ogni pacchetto inviato dalla HummBox verrà visualizzato sul portale TTN sotto forma di file JSON.

Il payload del pacchetto dati che riceveremo è composto da 5 byte:

| Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 |
| :--- | :--- | :--- | :--- | :--- |
| Tipo di pacchetto | Contatore (LSB) | Contatore (MSB) | Temperatura? | Batteria |

Nella sezione Payload Formatter di TTN è possibile scrivere il codice per interpretare il pacchetto appena viene ricevuto, il risultato di questa lettura viene collocato in un file JSON.

### AWS API Gateway

### AWS Lambda

### Database
