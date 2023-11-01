```table-of-contents
```
---

# Livello trasporto
Il livello di trasporto fornisce una serie di funzionalità cruciali per garantire che i dati vengano trasmessi in modo affidabile, sicuro ed efficiente all'interno di una rete di comunicazione.

Questo livello offre a quello applicativo una serie di paradigmi astratti per la comunicazione tra due processi: 
- **flusso di Byte** cioè fornisce una comunicazione continua di dati sotto forma di flusso di byte tra i due processi, 
- **scambio di messaggi** cioè garantirà che i messaggi vengano recapitati all'altro processo in modo affidabile, 
- **chiamata a funzione** cioè consente a un processo di chiamare una funzione o un metodo su un altro processo che si trova su una macchina remota.

Questo livello offre al livello applicativo una **interfaccia indipendente** dalle diverse tecnologie dello strato di rete (es IPv4, IPv6), però per completare le funzioni utilizza servizi dello **strato di rete**.

## Servizi
I servizi forniti del livello di trasporto sono due:
1. **Stram Sockets: Servizio affidabile orientato alla connessione - TCP**: è un protocollo affidabile che garantisce l'integrità, la completezza e l'ordine dei dati trasmessi tra due processi. Gli utenti di TCP vedono la connessione come una "pipe" virtuale attraverso la quale possono inviare e ricevere dati in modo affidabile e sequenziale.
2. **Datagram Sockets: Scambio inaffidabile di datagrammi - UDP**: è un protocollo di trasporto senza connessione, il che significa che non offre garanzie di consegna o ordine dei dati inviati. Se l'applicazione richiede un ordine specifico nell'invio di una sequenza di datagrammi, deve gestirlo autonomamente, poiché UDP non fornisce questo tipo di servizio.

---

## Demultiplexing - Multiplexing

### Demultiplexing
Nel processo di ricezione dei pacchetti dal livello rete, il livello di trasporto gestisce un indirizzamento che serve per associare il pacchetto IP in arrivo al processo applicativo a cui è destinato: analizza la porta di destinazione indicata nel pacchetto e smista il pacchetto al processo applicativo corretto.

La porta è un identificativo numerico (16 bit , 64K porte) che rappresenta il punto di arrivo di una connessione su di un host. La coppia (IPaddr., Port) identifica quindi univocamente un estremo di una connessione ed è detta **Socket**.
Una connessione tra gli host A e B è identificata da una coppia di socket: (IPaddrA, PortA) – (IPaddrB, portB). 

Le porte inferiori a 1024 sono dette “**Well-Known-Port**” e vengono universalmente associate alle principali applicazioni server da **IANA**, per agevolare l’identificazione del Socket server.
In diversi sistemi operativi le Well-Known-Ports possono essere assegnate solo da processi con privilegi. I processi server creati da utenti senza privilegi possono usare le porte non privilegiate (da 1025 a 32768).
Le porte da 32768 a 61000 sono dette **effimere**, assegnate dinamicamente ai processi client.

**Come trovo la porta?**
- Se il **servizio è standard** il server utilizza una “Well known port”, che tutti conoscono, o una porta non privilegiata.
- Per **servizi di rete dinamici** si può utilizzare un Name Server (Directory Server) con un servizio di PortMapper in ascolto su una Well Known Port, su cui i servizi di rete registrano la porta di ascolto (1) . Il client interroga il Portmapper per conoscere la porta del Server (2), quindi contatta il Server (3). Questo meccanismo è utilizzato dal protocollo RPC (Remote Procedure Call).

![[Client-Server.svg]]
### Segmentazione
Il mittente fraziona il flusso dell’applicazione in segmenti che avranno una dimensione massima detta MSS (Maximum Segment Size).
I segmenti vengono consegnati al livello Rete il quale si occuperà della consegna all'host di destinazione.
Se durante il tragitto viene incontrato un Link con MTU inferiore alla dimensione del pacchetto, il protocollo IP frammenterà il pacchetto in 2 o più parti, per poi ricomporle a destinazione.
Per evitare la frammentazione normalmente viene definito l’MSS in base al MTU dell'interfaccia locale (meno i byte dell'header TCP/UDP e i byte dell'header IP).

### Multiplexing
Nel processo di spedizione il dato viene eventualmente ridotto in segmenti (TPDU: Transport Protocol Data Unit) che vengono imbustati nell'header di trasporto con l'indicazione della porta di destinazione.

![[header_trasporto.svg]]

---

## Il modello client / server
Un estremo “**Server”** è sempre in ascolto su una porta stabilita, chiamata la primitiva `bind()` assegna un indirizzo locale (porta) ad un socket.

L'altro estremo "**Client**" prenderà contatto con il server specificandone il socket: per poter contattare il server, deve quindi conoscerne indirizzo IP e porta; quindi, la porta utilizzata dal client apparirà al server nell'intestazione di trasporto, dunque la porta del client non deve essere nota a priori. Generalmente viene determinata dinamicamente dal sistema operativo al momento della richiesta di connessione.

- Il client invia il messaggio con `sendto()` e riceve una porta dinamica dal sistema operativo per ricevere risposte.
- Il server si inizializza con `bind()` sulla sua porta di ascolto e utilizza `recvfrom()` per ricevere richieste dai client.
- Il client e il server comunicano attraverso le rispettive porte di destinazione e sorgente.

### Programmazione Servizi Connection-Oriented
Per connection-oriented significa che questi servizi hanno bisogno di instaurare una connessione prima del trasferimento dei pacchetti.
- `listen()` predispone le code di attesa per i processi client che accederanno contemporaneamente al servizio.
- `accept()` è una primitiva bloccante che consente al server di mettersi in ascolto sulla porta. Quando arriva una TPDU, il server crea un nuovo socket con le stesse proprietà di quello originale e ritorna un file descriptor per esso. Il server può creare un nuovo processo (fork) o un nuovo thread per gestire la connessione sul nuovo socket e tornare ad aspettare la prossima connessione.
- `connect()` è utilizzata dal client per aprire una connessione.

Quando la connessione è instaurata, la distinzione tra client e server non esiste più, anche se il primo invio di dati avviene fatto dal client.

---

## Protocollo TCP
Viene utilizzato per fornire un flusso di Byte *end-to-end* affidabile a partire da un servizio di rete inaffidabile (IP). 
Le connessioni TCP sono **full-duplex e unicast**.

Il protocollo riceve flussi di byte dai processi locali, li spezza in segmenti e li spedisce in datagrammi IP separati. 
L'applicazione che spedisce consegna i dati in un buffer di spedizione; questi byte possono essere raggruppati in segmenti da consegnare al livello di rete.

I segmenti sono di max 64KB, ma quasi sempre MSS = 1460 byte che, con le aggiunte degli header TCP e IP, arriva a 1500 che è come l’MTU di Ethernet.

Il flag "PUSH" può essere usato per l'invio non ritardato.
Il livello TCP di destinazione scrive i segmenti nel buffer di destinazione e consegna all'applicazione tutti i byte riscontrati (ricevuti in ordine), ricostruendo il flusso originale.

>*end-to-end significa che il flusso di byte parte e arriva ai nodi terminali senza riscontrare nodi intermedi.* 

**Problemi che possiamo incontrare:**
- ***Come si attiva e si chiude una connessione?***
- ***Come si controlla l'ordinamento dei dati?***
- ***Come si controlla il flusso?***
- ***Come si gestiscono gli eventuali errori o perdite di pacchetti?***

### Attivazione della connessione
La soluzione per applicare una connessione affidabile e senza errori è (l'handshaking a) **3 a tre vie**, vediamo il funzionamento:
1. Il client invia un segmento di Connection Request (CR) con un valore iniziale di sequenza.
2. Il server risponde con un ACK che riscontra il valore di sequenza proposto dal Client e propone un valore iniziale di sequenza per il senso inverso (da server a client).
3. Il client invia un terzo segmento con ACK e il riscontro della sequenza del server (che eventualmente può anche trasportare i primi dati).

> Molte analogie con il funzionamento del DHCP.

### Apertura di una connessione TCP
La soluzione che utilizza il protocollo TCP è derivata da quella precedente (handshaking a 3 vie) cioè:
1. La `Connect()` sul **client** invia un segmento con SYN = 1, ACK = 0, seq = x (random)
2. Se il **server** è in ascolto `listen()` e accetta la connessione, risponde con un segmento in cui ACK = 1, SYN = 1, ACKseq = x+1 (il destinatario riscontra il byte numero x e dichiara che x+1 è il prossimo byte che si aspetta di ricevere) e seq = y (random)
3. Il **client** termina l’apertura riscontrando la sequenza del server: ACK = 1, ACKseq = y+1

> Una *primitiva* e' una system call.
> SYN: questo segmento indica che il mittente desidera avviare una nuova connessione, serve per la sincronizzazione tra client e server.

### Chiusura della connessione TCP
In questo caso si utilizza un **handshaking a 2 vie** per ogni direzione:
1. La primitiva `close()`, inviata dal client, determina l'invio del FIN = 1 (finish), marca come chiuso il canale e che il client ha finito di inviare dati.
2. Il server riceve il segmento FIN e risponde con un segmento di conferma (ACK) per indicare che ha ricevuto il messaggio di chiusura del client, il server però può continuare a inviare dati.
3. Quando il server decide di chiudere la connessione, invia un segmento con il flag FIN al client.
4. Il client riceve il segmento FIN e risponde con un segmento di conferma (ACK) per indicare che ha ricevuto il messaggio di chiusura del server.

A questo punto subentra il TIME WAIT, cioè ciascuna parte entra in uno stato di attesa per un breve periodo di tempo, questo assicura che tutti i segmenti associati alla connessione siano stati completamente consegnati e che non vi siano segmenti persi in rete.
Ora la connessione è completamente chiusa e i socket associati vengono liberati.

### Consegna e ordinamento dei segmenti
Il **riscontro**, cioè la conferma dell'avvenuta ricezione di un segmento di dati, o anche detto ACKnowledgmement, abbinato al **numero di sequenza** attribuito ad ogni pacchetto dati o a ogni byte del flusso, rappresentano uno strumento molto utilizzato per la verifica della **corretta consegna dei pacchetti e del relativo ordinamento**.
Come funziona?
- Il mittente invia un **segmento di dati** assieme ad un numero progressivo.
- Il destinatario invia un pacchetto con un Flag (**ACK**) attivo e il numero del byte (o del segmento) ricevuto correttamente.
- Il mittente attiva un **Retransmission Time Out (RTO)** per ogni segmento inviato.

TCP per riordinare i dati usa la numerazione dei Byte:
- Il numero di sequenza è il numero del primo byte dei dati contenuti nel segmento.
- Il numero di riscontro, che accompagna l’ACK, è il numero del prossimo byte che il destinatario si aspetta di ricevere.
- Il numero iniziale della sequenza non è 0, ma è determinata in modo da evitare che in seguito alla reinizializzazione di una connessione si faccia confusione tra vecchi e nuovi pacchetti.
- Il mittente gestisce **un unico timer** per la ritrasmissione (**Retransmission Time Out - RTO)**, basato sul RTT e associato al più vecchio segmento non riscontrato. Quando arriva una notifica intermedia, si riavvia il timer sul più vecchio segmento non riscontrato.
- Se non riceve ACK di un segmento ricomincia a spedire dall'ultimo byte riscontrato (GoBack-N) a meno che non sia concordato il Selective ACK (TCP con SACK).

### Buffering
Per ogni connessione TCP è necessario un buffer (coda circolare) di trasmissione e un buffer di ricezione poiché i segmenti potrebbero andare perduti / fuori ordine e perché i processi di scrittura e lettura potrebbero lavorare a diverse velocità.

Il **buffer di trasmissione** contiene:
- Dati spediti ma non ancora riscontrati
- Dati ancora da spedire
- Spazio libero

Il **buffer di ricezione** contiene:
- Dati ricevuti e riscontati non ancora letti dall'applicazione
- Dati ricevuti non ancora riscontrati
- Spazio libero

### Socket NON Blocking
La `send()` **è per default bloccante**, si blocca quando il buffer in trasmissione è pieno e ritorna quando si libera spazio. 
Se lo spazio nel buffer è insufficiente per i dati da spedire viene effettuata una scrittura di una porzione di dati minore o uguale alla dimensione del buffer libero, e la `send()` restituisce il numero di byte scritti.
Se **il buffer è pieno** e il socket è impostato come **non bloccante** non ci sarà nessun blocco ma ritornerà un -1 settando la variabile di errore **EWOULDBLOCK .**

La `recv()` **è per default bloccante**, si blocca quando il buffer in ricezione è vuoto e ritorna quando ci sono dati nel buffer. 
Il numero di byte letti può essere inferiore al numero di byte richiesto.
**Ritorna 0** quando non ci sono dati nel buffer e l'altro peer ha chiuso la connessione.
Se il **buffer è vuoto** e il socket è impostato come **non bloccante** non ci sarà nessun blocco ma ritornerà un -1 settando la variabile di errore **EWOULDBLOCK**

### Controllo di Flusso
Lo **Sliding Window** viene utilizzato per il controllo del flusso e l'ottimizzazione del throughput della rete in TCP, come funziona?
- Il **Ricevente** annuncia al trasmettitore la **Receiver Window Size (rwnd)**, che generalmente corrisponde al numero di byte liberi sul buffer di ricezione e indica quanti byte possono essere inviati a partire dall'ultimo riscontrato.
- Il trasmettitore può inviare anche più dati senza riscontro, purché il numero di byte non riscontrati non ecceda.

> Receiver Window Size è la grandezza del buffer di ricezione, cioè quanti frame può ricevere in una volta.

---

## Trama TCP
![[frame-tcp.png]]
- **Porta di provenienza e destinazione** identificano gli estremi della connessione.
- Il **Numero Sequenziale** è il contatore del flusso di byte spediti, indica il numero del primo byte di dati contenuto nel segmento.
- Il **Numero di Riscontro** è il contatore del numero di byte ricevuti, indica il numero del prossimo byte che il destinatario si aspetta di ricevere.
- **HLEN** (parole di 32 bit dell'Header) è necessario perché il campo opzioni è variabile.

Dopo HLEN ci sono 4 bit riservati per sviluppi futuri, poi abbiamo 8 bit di codice, se attivi (posti a 1) significano:
- **CWR e ECE** vengono utilizzati quando è attivo ECN (gestione della congestione - RFC 3168)
	- **ECE (ECN-Echo):** usato per mandare ad un host l'indicazione di rallentare.
	- **CWR** e' generato dall'host per indicare che ha ridotto la finestra di congestione.
- **URG**: si deve considerare il campo “**puntatore urgente**”.
- **ACK** : si deve considerare il “**numero di riscontro**”.
- **PSH** : il ricevente non deve bufferizzare, ma renderli subito disponibili all'applicazione
- **RST**: reset della connessione a causa di qualche tipo di problema.
- **SYN**: utilizzato nella fase di attivazione di una connessione.
- **FIN** : utilizzato nella fase di rilascio di una connessione.

- **Finestra** (16 bit): è la dimensione della Sliding Window, ovvero il numero di byte che il destinatario è in grado di ricevere a partire dall’ultimo byte riscontrato.
   La dimensione massima sarebbe di 64KB , ma può essere aumentata attraverso il fattore di Scala della Finestra (vedi opzioni).
- Il **CheckSum** (16 bit): somma in complemento a 1 delle sequenze di 16 bit del segmento TCP (header e dati) e la “pseudo-intestazione”.
- La **pseudo-intestazione** include ulteriori informazioni importanti di IP e TCP (IP source, IP dest, 0x00, 0x06, TCP Segment length), violando però l'indipendenza dei protocolli perché include dati del Layer IP.

I campi opzionali dell’intestazione TCP vengono principalmente utilizzati nella fase di Handshake, nei segmenti SYN, per comunicare all'altro capo una serie di parametri utili a regolare la connessione.
Normalmente vengono usate le seguenti opzioni:
- **MSS:** massima dimensione accettata del segmento
- **SACK**: Selective ACKnowledgement
- **Fattore di scala della finestra**
- **timestamp**: (**TSval** , timestamp value)

Se i byte delle opzioni non sono multipli di 4 (parole di 32 bit) viene aggiunto un padding opportuno.

### Opzione MSS - Maximum Segment Size
Questa opzione viene utilizzata per **concordare l’MSS ottimale**, la frammentazione introduce un **overhead sull'attività dei router**, cioè frammenti troppo piccoli determinano un **overhead sul traffico di rete** (lavoro extra).
Il MSS ottimale dipende dall'MTU minimo tra tutti gli MTU incontrarti nel tragitto, però questo dato non è noto quando si inizia una trasmissione e potrebbe cambiare nel tempo.

>*l'**MTU** riguarda la dimensione massima di un pacchetto che può essere trasmesso su una rete, mentre l'**MSS** riguarda la dimensione massima di un segmento di dati all'interno di un pacchetto TCP*

### Opzione SACK - Selective ACK
Per default TCP funziona con **GoBackN**: se il ricevente ottiene un segmento errato e N segmenti validi, riscontra sempre l'ultimo segmento valido prima dell'errore, questo manda in TimeOut il mittente che rimanda tutti i Segmenti a partire da quello errato.
Per migliorare le prestazioni evitando la ritrasmissione di segmenti validi è stata proposta la tecnica **SACK**, il ricevitore indica al trasmettitore quali segmenti sono arrivati correttamente in modo che possa determinare quali segmenti devono essere rispediti.
Abbiamo due opzioni dell'header TCP:
1. SACK permitted: viene incluso in un segmento SYN per indicare la capacità di gestire la tecnica SACK
2. SACK: viene utilizzato dal ricevente per comunicare le informazioni SACK (i segmenti ricevuti correttamente).

### Opzionale Window Scale e timestamp
La dimensione della finestra è scritta in un campo di 16 bit (2Byte), consentendo quindi un valore massimo di 64KB (2^16), nelle reti moderne questa dimensione massima è insufficiente. 
L’opzione **window scale** determina numero di shift a sinistra da applicare nell’interpretare il valore ricevuto, ogni shift a sinistra corrisponde al una moltiplicazione 2x.
Ad esempio con Window Scale = 2 il valore massimo delle finestra è di 256KB.

**Timestamp**: (**TSval** , timestamp value) è un marcatore temporale spedito dal mettente e rimbalzato poi dal destinatario ( **TSecr** , timestamp echo reply), per il calcolo del RTT (RTT = current time – TSecr).

---

## ACK Delay e ACK cumulativo
**Delayed ACK**: quando il destinatario riceve un segmento in ordine può attendere fino a 500ms per l’arrivo del prossimo segmento.

**ACK cumulativo**: se durante l’attesa arriva un altro segmento in ordine risponde con un singolo **ACK cumulativo** che riscontra l’ultimo byte della sequenza.
Questa tecnica è utilizzata in molte implementazioni di TCP.

### Fast Retrasmission
Se il destinatario riceve un segmento fuori ordine (successivo ad altri segmenti non ricevuti) invia un ACK in cui viene riscontrato l’ultimo segmento ricevuto in ordine.
Quando il mittente riceve 3 ACK che riscontrano lo stesso numero capisce che un segmento è andato perduto e lo ritrasmette, senza attendere lo scadere del timer (Fast Retransmission).
Il destinatario risponde con un singolo ACK che riscontra anche i successivi segmenti ordinati (ACK cumulativo).

## Algoritmo di Nagle e soluzioni di Clark
Le prestazioni possono degradare in alcuni casi particolari, quali:
- **Il trasmettitore genera dati lentamente**: ad esempio quando si edita un file per ogni tasto premuto girano 4 pacchetti IP per un totale di 162 byte.
- **Il ricevitore consuma dati lentamente**: ad esempio il destinatario pubblica finestre di pochi byte, perché l'applicazione legge pochi byte per volta, il mittente è costretto a spezzare il flusso in tanti segmenti (problema della finestra futile).

Per attenuare il problema a lato mittente (trasmettitore) si usa **l'algoritmo di Nagle**:
- se il mittente ha **pochi byte da spedire** (a causa dell'applicazione o della finestra del destinatario) e **ci sono dati non riscontrati →** aspetta ACK, anche se la finestra scorrevole consentirebbe l’invio di altri dati.
- se il mittente ha **molti byte da spedire** oppure i **segmenti piccoli sono riscontrati** → spedisci subito.

>Questo algoritmo può essere disabilitato con l’opzione **TCP_NODELAY**.
>Esempio in C: `setsockopt (sock, SOL_TCP, TCP_NODELAY, … );`

Per attenuare il problema lato ricevente si usa la **soluzione di Clark**:
- Se il ricevente pubblica finestre troppo piccole l'algoritmo forza il ricevitore ad attendere che la finestra raggiunga un valore minimo prima di comunicarlo al mittente.

---

## RTO - Retrasmission Time Out
Serve per decidere quando un pacchetto deve considerarsi perduto, deve essere almeno pari a RTT, ma deve aggiornarsi dinamicamente e deve gestire situazioni di congestione (backoff).

**Algoritmo di Jacobson**
Se l'ACK torna indietro prima dello scadere dell'RTO l'algoritmo calcola il valore del RTT (Round Trip Time) e aggiorna le variabili:

- $RTTMedio = α RTTMedio + (1-α) RTT$
- $DevMedia = α\; DevMedia + (1-α)\; abs(RTT - RTTMedio)$ → *(α e' il peso che si vuole dare ai precedenti valori medi, valore tipico 0.9)*
- $RTO = RTTMedio + 4 x DevMedia$

**Algoritmo di Backoff (di Karn)**
Per le reti congestionate, se l'RTO scade significa che la rete è congestionata; in questo caso l'algoritmo di Karn prevede di non aggiornare L'RTTMedio e raddoppiare l' RTO fino a quando i segmenti non arrivano a destinazione al primo tentativo.
$$RTO (i+1) = 2 * RTO(i)\; \text{ backoff esponenziale binario}$$

### Altri timer in TCP
Oltre a RTO, che è il più importante, TCP gestisce altri Timer:
- **Timer di Persistenza**: viene attivato quando la finestra viene chiusa (rwnd=0). Se il pacchetto che riapre va perduto, allo scadere del timer il mittente invia una “window probe” che sollecita la rispedizione della finestra. Se la finestra è ancora 0 il timer viene reimpostato.
- **Timed Wait**: Tempo di attesa dopo un FIN. Prima di rilasciare la connessione viene attivato questo timer per gestire eventuali pacchetti circolanti dopo la chiusura.
   Generalmente corrisponde a doppio del tempo di vita massimo di un pacchetto.
- **Timer di Keepalive:** parte quando la linea TCP è inattiva. Se arriva a zero TCP invia un ACK; se non riceve risposta la connessione viene considerata interrotta.

---

## Protocollo UDP
Offre alle applicazioni un modo per inviare datagrammi senza dover stabilire una connessione, l'unica differenza importante rispetto a IP è l'aggiunta delle porte di origine e destinazione necessarie per il demultiplexing.
L'intestazione UDP contiene inoltre la lunghezza del segmento (header + dati) e il checksum facoltativo (che è la somma delle sequenze di 16 bit in complemento a 1).
Questo tipo di protocollo viene utilizzato per:
1. L'implementazione di protocolli applicativi che richiedono lo scambio di brevi messaggi (esempi: DHCP, DNS, TFTP).
2. La costruzione di servizi di trasporto più astratti, a livello applicativo, denominati **Protocolli Middlewere**.
3. Comunicazione multicast o broadcast.

