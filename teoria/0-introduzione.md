# Introduzione - Reti di Calcolatori

Una **rete di calcolatori** è un insieme di nodi di elaborazione **autonomi** tra loro e **connessi** mediante un opportuno sistema di comunicazione, in grado di interagire attraverso scambio di messaggi al fine di consentire alle applicazioni in esecuzione sui nodi di comunicare tra loro.

La comunicazione avviene tramite 5 componenti:
- **Messaggio**
- **Mittente**
- **Destinatario**
- **Mezzo di trasmissione**
- **Protocollo**

Per valutare un canale di comunicazione ho bisogno di considerare alcune metriche:
- **Ampiezza di banda digitale (bit/sec)**: Quantità di bit (dati) che possono essere trasmessi nell'unità di tempo (sec)
- **Ritardo/Latenza (sec)**: Tempo di trasferimento di un bit da un terminale all'altro
- **Jitter**: Variazione del ritardo
- **Affidabilità**: Intolleranza agli errori di trasmissione, o meglio la percentuale di bit persi
- **Sicurezza**: Capacità di opporsi ad accessi non autorizzato, danno o violazioni della rete

| Applicazioni  | Affidabilità | Ritardo | Jitter | Larghezza di banda |
| ------------- | ------------ | ------- | ------ | ------------------ |
| E-mail        | Alto         | Basso   | Basso  | Basso              |
| File transfer | Alto         | Basso   | Baso   | Medio              |
| Web access    | Alto         | Medio   | Basso  | Medio              |
| Remote login  | Alto         | Medio   | Medio  | Basso              |

Due nodi comunicano mediante una connessione fisica, se è presente un canale fisico che li collega direttamente; una catena di canali fisici forma una connessione logica su di un percorso detto canale virtuale.
In una connessione i nodi possono essere terminali o di transito.

![[Nodi.svg]]

Ogni link (collegamento) ha la propria ampiezza di banda e latenza, la velocità di trasmissione sul canale virtuale (throughput) non potrà superare l'ampiezza di banda del link più lento.
E' possibile attivare più canali virtuali contemporaneamente sullo stesso link utilizzando una tecnica di condivisione del canale (multiplexing). 
L'ampiezza di banda del link viene quindi condivisa tra i diversi canali virtuali.

**Alcune definizioni importanti**
- **Link**: è un canale di comunicazione che interconnette fisicamente due nodi
- **Path**: è la catena di link che compone un canale virtuale tra due nodi
- **Hops**: è il numero di link da attaversare
- **Diametro**: è la distanza (hops) tra due nodi più lontani
- **Grado**: numero massimo di link connessi ad un nodo
- **Scalabilità**: capacità della topologia di poter aggiungere o rimuovere nodi

Caratteristiche che può avere un canale:
<mark style="background: #946EFA"> Direzione: </mark>
- **Simplex**: monodirezionale (TV)
- **Half-Duplex**: entrambe le direzioni, non contenporaneamente (walkie-talkie)
- **Full-Duplex**: entrambe le direzioni, contemporaneamente (telefono)
<mark style="background: #946EFA"> Destinazione: </mark>
- **Unicast**: un singolo destinatario
- **Broadcast**: tutti i nodi appartenenti ad una rete o sottorete
- **Multi-cast**: un sotto insieme dei nodi della rete
<mark style="background: #946EFA"> Canali di comunicazione: </mark>
- **Punto-Punto**: comunicazione tra due nodi (fibra ottica, doppino)

![[Punto_Punto.svg]]

- **Multi-Accesso**: comunicazione tra n nodi tramite bus (wireless)

![[MultiAccesso.svg]]
## LAN (Local Area Network)

I mezzi trasmissivi multi-accesso possono essere utilizzati per realizzare un particolare tipo di rete detta LAN (Local Area Network) che include tutti i nodi che condividono lo stesso canale.
Questa rete supporta tutti i modelli di destinazione: Unicast, Broadcast, Multicast e dispone di un opportuno protocollo per disciplinare l'accesso al canale e per gestire l'indirizzamento dei pacchetti.
Solitamente la tecnologia **Ethernet** è la dominante per questo tipo di reti, ottenendo così una topologia o a stella o ad albero.

## WAN (Wide Area Network)

Per realizzare reti che si estendano su grandi distanze geografiche si possono utilizzare semplici collegamenti punto a punto (ADSL: tra casa e centrale telefonica).

## Commutazione
Il processo per individuare ed utilizzare il percorso su cui far transitare i messaggi/pacchetti su un canale virtuale è detto commutazione e ne esistono di due tipi:
- #### Commutazione di circuito (reti telefoniche)
	Viene individuato il percorso tra i due terminali e creato un circuito fisico temporaneo, ovviamente si presenterà un ritardo iniziale dovuto al tempo necessario per instaurare il circuito. 
	I terminali scambiano i dati (come se fosse un collegamento diretto) e il canale viene chiuso al termine della comunicazione.
- #### Commutazione di pacchetto (reti di dati)
	I dati della comunicazione sono frazionati in “pacchetti” con una lunghezza massima stabilita, i nodi di transito (router, switch, ..) hanno il compito di instradare ogni pacchetto. 
	Il destinatario li riassembla e ricostruisce il messaggio.

## ISO-OSI - Architettura a strati


![[ISO-OSI.svg]]

L'architettura a strati ha alcuni vantaggi:
- Scompone il problema in sotto-problemi posti a diversi livelli, più semplici da trattare.
- Rende i vari livelli indipendenti, comunicanti mediante un'interfaccia standard.
- Strati diversi possono essere sviluppati da enti diversi.

ISO-OSI scompone la comunicazione in 7 livelli, lo scopo di ciascun strato è quello di fornire servizi agli strati superiori utilizzando i servizi forniti dai livelli inferiori.
### Layer:
[[1-livello_fisico]]
[[2-livello_collegamento]]
[[3 - Livello Rete]]
[[4 - Livello Trasporto]]
[[5 - Livello Sessione]]
[[6 - Livello Presentazione]]
[[7 - Livello Applicazione]]

>***Critiche del modello OSI***
>  - *Poca tempestività*: OSI arriva quando il modello TCP/IP era già diffuso.
>  - *Tecnologia scadente:* La scelta di 7 livelli era più politica che tecnica, due livelli quasi vuoti (Presentazione e Sessione) e due troppo pieni (Collegamento e Rete).
>  - *Implementazioni carenti:* Prime implementazioni lente, complicate ed enormi, al contrario TCP/IP era semplice veloce e Open (parte di Unix)
>  - *Incapacità politica:* Sviluppi dominati dalle Telecom, Ministeri, Comunità Europea e USA, percepito con un insieme di standard imposti da burocrati.

## TCP/IP

![[TCP-IP.svg]]

Rispetto al modello OSI abbiamo che il TCP/IP ha condensato il livello rete e collegamento nel primo layer e non troviamo più i livelli Presentazione e Sessione.

>Vedi appunti TCP/IP per la spiegazione dettagliata