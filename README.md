# Replicare il sistema
Qui saranno riportate istruzioni per replicare il sistema
## Indice
  1) Dispositivi fisici
  2) TTN
  3) Gateway LoRa
  4) AWS

## Dispositivi fisici
### Sensore e HummBox
  - Inserire l'antenna alla HummBox
  - Collegare il connettore M12 del sensore pluviometrico alla rispettiva porta nella HummBox
### Gateway LoRa
  - Inserire le antenne
  - Collega alimentazione
  - Connettere la porta sul retro ad un router mediante un cavo Ethernet.

## TTN
Una volta registrati su The Things Network è necessario:

### Registrare un end device
Per registrare l'end device è necessario:
  - Scegliere un id univoco per la nostra Application
  - Imposta AppEUI, DevEUI e AppKey
  - Frequency Plan: `Europe 863-870 MHz (SF9 for RX2)`
  - LoRaWAN Version: `LoRaWAN Specification 1.0.2`
  - Regional Parameters Version: `RP001 Regional Parameters 1.0.2`

### Configurazione
Una volta registrato l'end device mandare in downlink il seguente messaggio: `00 01 01 00 02 0E 00 37`

In seguito accedere alla sezione *Payload Formatter* e caricare il codice contenuto in questa repository.

## Gateway LoRa
Per configurare il Gateway LoRa:
  - Accedere al portale `https://rg1xx??????.local`, al posto dei punti interrogativi inserire gli ultimi 6 caratteri del MAC Address presente sul retro del dispositivo
  - Dalla sezione *Impostazioni* caricare la configurazione contenuta in questa repository
  - Dal sito TTN impostare un nuovo Gateway caricando la configurazione contenuta in questa repository.

## AWS
### AWS API Gateway
  - Importare il file di configurazione dell'API contenuto in questa repository.
  - Dal sito TTN inserire un nuovo WebHook di tipo JSON con il BaseURL strutturato così: `URL_FORNITO_DA_AWS/dati`
