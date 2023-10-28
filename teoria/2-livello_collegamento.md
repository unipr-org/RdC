```table-of-contents
```
---

# Livello Data - Link
Il livello Data-Link è responsabile di fornire un mezzo affidabile per il trasferimento di dati tra nodi adiacenti in una rete di computer. Questi nodi possono essere collegati attraverso canali punto-punto o su una rete multi-accesso.
Per garantire una comunicazione affidabile, il livello Data-Link suddivide il flusso di dati in unità discrete chiamate <mark style="background: #946EFA;">frame.</mark> Un frame è un pacchetto di dati di lunghezza massima fissa o prefissata, questo processo di suddivisione aiuta a gestire in modo più efficiente la trasmissione dei dati sulla rete.
Ogni frame è composto da tre parti principali:
1. **Header**: è la parte iniziale del frame e contiene le informazioni di controllo necessarie per il corretto indirizzamento e la gestione della trasmissione, può includere informazioni come gli indirizzi del mittente e del destinatario, i controlli di errore e altre informazioni di controllo.
2. **Payload**: è la parte del frame che contiene i dati veri e propri che devono essere trasmessi; essi sono provenienti dal livello superiore (rete) e rappresentano l'informazione utile da consegnare al nodo di destinazione.
3. **Trailer**: è la parte finale del frame e contiene ulteriori informazioni di servizio, come i controlli di errore utilizzati per verificare l'integrità dei dati durante la trasmissione.

Una volta che il frame è stato creato con il payload e le informazioni di servizio appropriate, viene trasmesso attraverso il mezzo di comunicazione verso il nodo di destinazione, qui, il nodo ricevente decodifica l'header per ottenere le informazioni di controllo necessarie e il payload per estrarre i dati. Vengono eseguite anche le verifiche degli errori utilizzando le informazioni di servizio nel trailer.

![[Pacchetto.svg]]

---
## Servizi offerti al livello Network (Rete)
Vediamo i diversi tipi di servizi che possono essere forniti al livello di rete nel contesto del livello Data-Link:
- [[#Protocolli in modalità non connessa]]
	- **Senza connessione e senza conferma**: Questo servizio non richiede di stabilire una connessione prima di trasmettere i dati, è veloce e semplice, adatto per mezzi di comunicazione affidabili come Ethernet, dove la perdita di dati è rara.
	- **Senza connessione ma con conferma**: In questo caso, non è necessario stabilire una connessione prima della trasmissione, ma viene inviato un messaggio di conferma per ogni frame inviato, questo servizio è utile quando il mezzo di comunicazione non è molto affidabile, come ad esempio in una rete LAN wireless.
- [[#Protocolli in modalità connessa]]
	- **Con connessione e con conferma**: Questo servizio richiede l'attivazione di una connessione prima della trasmissione dei dati; ogni frame inviato è numerato, il che permette di garantire che ogni frame venga ricevuto una sola volta e nell'ordine corretto.
	  Il processo comprende tre fasi distinte:
	  - Attivazione della connessione
	  - Invio dati numerati e conferme
	  - Chiusura della connessione
	 Tuttavia, questo servizio ha un overhead elevato e di solito non è comunemente utilizzato a livello Data-Link. È più comunemente implementato a livelli superiori, come nel protocollo TCP, che opera a livello di trasporto.


---

## Impacchettamento (Framing)
Il primo problema da risolvere è come delimitare inizio e fine di un frame, come detto precedentemente, i frame possono avere dimensione fissa o variabile, se è fissa non è necessario delimitare il frame, altrimenti, se è variabile, occorre una strategia per distinguerli, vediamole:
1. Un livello **temporale** tra un frame ed il successivo
2. Far precedere ogni frame con un **numero di byte del frame**
3. Delimitare il frame con caratteri speciali **Flag**
La maggior parte dei protocolli Data-Link utilizza l'abbinamento delle soluzioni Flag e Temporale.

### Delimitare il frame con un Flag
La delimitazione del frame è marcata da un Byte speciale denominato **Flag**.
Tuttavia, sorge un problema quando la sequenza di byte all'interno del frame include accidentalmente il byte FLAG, questo potrebbe causare confusione nel ricevente, che potrebbe erroneamente interpretare la fine del frame prima del tempo.
Per evitare questo problema, si utilizza una tecnica chiamata  <mark style="background: #946EFA;">Byte Stuffing.</mark> Nel caso di flussi di dati orientati ai byte, quando viene rilevata la sequenza flag, viene inserito un **byte di escape** (denominato "ESC") appena prima dell'occorrenza del FLAG.
Il destinatario della trasmissione deve poi eseguire l'operazione di **destuffing** per interpretare correttamente i dati, questo significa che il destinatario identifica la sequenza ESC+FLAG e rimuove il byte di escape, mantenendo solo il byte FLAG originale.
Così, il destinatario può correttamente delimitare i frame, anche se il byte FLAG è presente all'interno del payload del frame stesso; questa tecnica è essenziale per garantire che la comunicazione avvenga in modo affidabile e senza ambiguità nel livello Data-Link.

![[Frame.svg]]

Se i flussi sono **Bit-Oriented** si può utilizzare il <mark style="background: #946EFA;">Bit Stuffing</mark>, cioè ogni frame inizia e termina con la sequenza 01111110 che sarebbe il Flag e ogni volta che nella trama si incontra la sequenza 11111 (5 uni) viene aggiunto un bit 0, cioè il bit stuffing, per non confondere il destinatario.

---
<p style="color: #946EFA;">Esempio: </p>
Flusso iniziale: 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0
Aggiunta dei stuffed bits: 0 1 1 1 1 1 <span style="color: #946EFA;">0</span> 1 1 1 1 1 <span style="color: #946EFA;">0</span> 1 1 1 1 1 <span style="color: #946EFA;">0</span> 1 0 0 1 0
Flusso elaborato dal destinatario: 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0

---

## Rilevazione e Correzione degli errori
Durante la trasmissione di un frame possono verificarsi disturbi o rumore termico che possono cambiare la forma del segnale e quindi alterare la ricezione dei bit.
Gli errori sono rari su linee ottiche, mentre possono essere frequenti su canali come wireless o “ultimo miglio” sulla linea ADSL.
Tipi di errori:
- A bit singolo
- A raffica (burst)
Per individuare gli errori si utilizza la **Ridondanza**, cioè il mittente, attraverso un opportuno algoritmo, determina un breve codice (FCS - Frame Control Sequence), che verrà inviato assieme al frame; se il destinatario riapplicando l'algoritmo otterrà una sequenza FCS diversa capirà che si è verificato un errore.

Ci si affaccia in due modi alla verifica degli errori:
1. **Rivelazione degli errori senza correzioni**: Richiede algoritmi più semplici ed un FCS più breve; si utilizza su canali affidabili (Fibra ottica), in cui gli errori sono rari e conviene eventualmente *ritrasmettere* il frame.
    *La richiesta di ritrasmettere il frame può essere esplicita (NACK) o automatica attraverso l'utilizzo di un timer.*
2. **Rilevazione e correzione degli errori**: Richiede algoritmi più complessi e maggiore ridondanza nel FCS; si utilizza raramente, in reti poco affidabili o in trasmissioni Simplex, in cui non è possibile inviare al mittente la richiesta di ritrasmissione.

<span style="color: #946EFA; font-weight: bold;">Vediamo i possibili algoritmi: </span>
### Bit di parità (poco efficiente)
E' un semplice algoritmo di rilevazione dell'errore, come funziona?
L'idea di base è quella di aggiungere un bit extra, chiamato **bit di parità**, alla sequenza di bit che si sta trasmettendo, questo bit è scelto in modo che il numero totale di 1 nella sequenza, includendo il bit di parità stesso, sia o pari o dispari (dipende dall'esigenza della rete o del sistema).
Questo algoritmo applicato alla sequenza di un frame determina l’esistenza di un singolo errore all’interno della sequenza.
Il bit di parità si usa in molti dispositivi hardware come ad esempio nei bus SCSI e USB e in molte cache di microprocessori.

### Cyclic Redundancy Check (CRC)
Come funziona?
- **Rappresentazione del frame come polinomio**: innanzitutto devo rappresentare il frame di lunghezza *d* bit come una lista di coefficienti di un polinomio *D* con *d* termini (di grado d−1). Ad esempio, la sequenza 110001110001 rappresenta $x^{11}+x^{10}+x^6+x^5+x^4+x^0$.
- **Scelta del polinomio generatore**: successivamente il trasmettitore e il ricevitore concordano su un polinomio comune *G* di grado r (quindi r+1 bit), detto **generatore**, questo polinomio deve essere di grado un numero primo.
- **Aggiunta del CRC**: il trasmettitore aggiunge *r* bit al termine della sequenza del frame, formando un nuovo frame *M* di grado r + d−1; questi *r* bit costituiscono il CRC e sono inizialmente impostati a 0.
- **Divisione polinomiale**: il trasmettitore esegue una divisione polinomiale modulo *G* tra il polinomio rappresentato dal frame con CRC aggiunto (*M*) e il generatore *G*. Il risultato è il quoziente *Q* e il resto *R*.
- **Aggiornamento del CRC** : il trasmettitore sostituisce i *r* bit di CRC con il resto *R* della divisione polinomiale modulo *G*.
- **Trasmissione**: il frame *M* con il nuovo CRC è trasmesso attraverso il canale di comunicazione.

Alla ricezione, il destinatario esegue gli stessi passaggi:

1. **Rappresentazione del frame come un Polinomio**: il frame ricevuto viene rappresentato come un polinomio.
3. **Divisione Polinomiale Modulo G**: il ricevitore esegue una divisione polinomiale modulo *G* tra il polinomio ricevuto e il generatore *G*. Il risultato è il quoziente *Q* e il resto *R*.
4. **Controllo dell'Errore**: il ricevitore verifica se il resto *R* della divisione è diverso da zero; se è diverso da zero, significa che si è verificato un errore durante la trasmissione.

>Vantaggi: i moduli di codifica e decodifica possono essere facilmente implementati in hardware.
>Il CRC è il codice più utilizzato nei protocolli data-link.

### Checksum (Somme di controllo)
Si basa sulla rappresentazione dei numeri in complemento a 1 per individuare differenze tra i bit inviati da mittente e quelli ricevuti dal destinatario.
Come funziona?
Il mittente divide il segmento in blocchi da 16 bit e li somma, quindi ne fa il complemento (inverto i bit 0 -> 1, 1 -> 0) e inserisce il risultato nel campo checksum.
Il ricevente ricalcola il checksum (includendo il checksum ricevuto) senza complemento finale.
Il risultato, senza errori di trasmissione è una sequenza di 1, altrimenti c’è un errore.

>adatto per l'implementazione software e per questo non è usato a livello Data-Link ma nei livelli superiori.

*Attenzione: il termine **Checksum** è spesso utilizzato per intendere in generale le tecniche per verificare l'integrità di un dato o di un messaggio.*

----

<span style="color: #946EFA;">Esempio:</span> 

![[checksum.svg]]

---

## Protocolli per il controllo del flusso
Il protocollo è un insieme di regole che devono essere rispettate per fare in modo che il tutto vada a buon fine; abbiamo quindi protocolli condivisi tra mittente e destinatario per garantire il corretto invio del flusso dei dati.
Possono essere implementati al livello Data-Link o superiori.

### Protocolli in modalità non connessa
Vengono applicati a canali che non hanno la necessità di essere sempre connessi e che sono senza rumore
- <span style="color: #946EFA;">Protocollo semplice:</span>  non ho bisogno di attendere un feedback dal destinatario.
- <span style="color: #946EFA;">Protocollo Stop-and-wait:</span> in questo caso ho bisogno di attendere un feedback dal destinatario prima di inviare il prossimo frame.
### Protocolli in modalità connessa
- <span style="color: #946EFA;">Protocollo Stop-and-wait ARQ:</span> il mittente attiva un timer per ogni frame inviato, se il mittente non riceve un ACK (un feedback di conferma) in un certo tempo il frame viene rispedito.
- <span style="color: #946EFA;">Protocolli a finestra scorrevole:</span> (Sliding Window): migliorano l'efficienza del canale consentendo al trasmettitore di poter inviare fino SWS (Sender Window Size = numero di frame inviati consecutivamente prima di attendere l'ACK) frame senza attendere il riscontro ACK.
   I frame appartenenti alla finestra vengono memorizzati dal mittente per eventuali ritrasmissioni.
   Il mittente assegna ad ogni frame un **numero di Sequenza**, l’indice LFS (Last Frame Sent) contiene il numero dell’ultimo frame inviato, l'indice LAR (Last Ack Received) contiene l’indice dell’ultimo ACK ricevuto; deve valere la regola LFS-LAR <= SWS.
   Il destinatario può comunicare al mittente la **finestra del destinatario**, che specifica il numero di dati che il destinatario può ricevere in quel momento, in genere corrisponde allo **spazio libero nel buffer del ricevente**.
   La **finestra utilizzata del mittente** non può superare la finestra del destinatario ma può essere ridotta per altri motivi che vedremo più avanti.
   
   Protocollo per il recupero di **errori**:
	- Go-Back-N ARQ: Se il mittente non riceve un ACK entro un certo timeout o riceve un ACK negativo (NACK), si assume che sia avvenuto un errore o una perdita di dati. In questo caso, il mittente ricomincia la trasmissione dal primo frame non confermato (con numero di sequenza successivo) e tutti i frame successivi.
	   Mentre è possibile ricevere un ACK fuori sequenza e quindi: se il mittente riceve un ACK per un frame successivo a quello atteso, tutti i frame precedenti devono essere ritrasmessi. Questo garantisce che il destinatario riceva i dati in ordine corretto.
	- Ripetizione Selettiva: i frame ricevuti correttamente, successivi a quello errato o perduto, vengono bufferizzati dal ricevente il quale sollecita il mittente al reinvio dei frame mancanti, tramite l'invio di un NACK.

### Esempi di protocolli per il livello data-link
**HDLC**: Utilizzato in ADSL, è un protocollo data link bit-oriented nato per comunicazioni punto-punto o multi-punto, con supporto sia alla modalità non connessa che connessa.
**PPP (Point to Point Protocol)**:  è protocollo Byte Oriented, supporta solo la modalità non connessa e vari protocolli dello strato rete; gestisce protocolli ausiliari (LCP e NCP) per l'autenticazione, la configurazione degli indirizzi di rete (IP via DHCP) e la concatenazione di diversi link.

### PPP - Point to Point Protocol
Il frame PPP aggiunge una intestazione di 6 (o 8) byte al payload, in cui vengono definiti alcuni campi originariamente ideati per HDLC.

![[PPP.svg]]

In questo protocollo abbiamo che il framing è gestito con il flag 01111110, mentre i campi address e control derivano da HDLC e in PPP hanno un valore fisso, il campo protocol è stato aggiunto per supportare diversi protocolli a livello rete o protocolli ausiliari (LCP e NCP) e il Payload contiene un numero variabile di Byte.

>*Nota: Il protocollo ausiliario **LCP** è utilizzato per configurare e verificare la connessione a livello data-link e consente di concatenare diversi link PPP.
>Il protocollo ausiliario **NCP** serve per configurare i diversi protocolli di livello Network come DHCP per gli indirizzi di rete, per la compressione.*

#### PPP applicato su ATM (PPPoA)
Le Telecom forniscono connessioni geografiche utilizzando le proprie reti commutate basate su tecnologia [[#ATM - Asyncronous Transfer Mode]].
ATM è una rete a commutazione di pacchetti, dette celle, di lunghezza fissa di 53 Byte, di cui 48 di payload.
Lo standard PPPoA definisce le modalità per trasportare pacchetti PPP all'interno di celle ATM, PPP riceve frame Ethernet per questo  utilizza lo stesso MTU (dimensione massima di un pacchetto di dati) di 1500 Byte.
Il frame PPP viene suddiviso in celle da 48 Byte e riassemblato all'uscita della rete ATM.

---

## ATM - Asyncronous Transfer Mode
E' una tecnologia di rete che è stata originariamente progettata per gestire la trasmissione di dati a commutazione di pacchetto attraverso la rete telefonica. Tuttavia, è stata sviluppata con l'ambizione di essere utilizzata anche per le comunicazioni Internet.
Nascendo dal mondo della telefonia, abbiamo quindi bisogno di adattare i principi di base dell'architettura a questo tipo di esigenza (Internet), come?
- **Commutazione di pacchetto a circuito virtuale**: prima che i dati vengano trasmessi, viene stabilito un percorso "virtuale" dedicato attraverso la rete tra mittente e destinatario.
- **Qualità del servizio**: le trasmissioni telefoniche vengono integrate nelle trasmissioni dati, ma hanno diversi requisiti di qualità.
- **Pacchetti (celle) di lunghezza fissa di 53 Byte** di cui 5 di intestazione e 48 di payload.

>ATM non ha avuto successo al di fuori delle reti telefoniche, se non per la realizzazione di reti WAN, viceversa la telefonia sta diventando sempre più una applicazione di Internet.

---

## Local Area Network
Un canale Multi-Accesso (o canale broadcast) è un canale condiviso per l'accesso diretto tra più terminali ed è il modo più semplice per realizzare una rete di calcolatori a livello Data-Link: <mark style="background: #946EFA;">LAN</mark>, che fanno parte dello stesso **dominio di broadcast** in cui i terminali possono scambiare tra loro messaggio unicast o broadcast.
Le problematiche delle reti LAN richiedono la definizione di un protocollo specifico per:
- Disciplinare l’accesso al canale (se fisicamente broadcast)
- Gestire gli indirizzamenti unicast, broadcast e multicast

### Accesso al canale
Il canale può essere assegnato agli utenti in modo **statico** o **dinamico**.
Allocazione **statica** del canale: si può realizzare con tecniche FDM e TDM (vedi [[1-livello_fisico#MULTIPLEXING]]) suddividendo la capacità trasmissiva del canale in sotto-canali di numero e dimensione prestabilita.
Se il numero di utenti è inferiore al numero di canali ho uno spreco di banda, se il numero di utenti è superiore, alcuni utenti non possono parlare, anche se altri stanno sottoutilizzando il proprio slot.
Questa tecnica è poco efficiente per le Reti Locali in cui gli utenti e le loro esigenze mutano rapidamente, quindi l'assegnazione del canale nelle principali tecnologie LAN è <mark style="background: #946EFA;">dinamica.</mark>

### Accesso Multiplo
Un singolo canale viene condiviso da N stazioni, ma viene utilizzato solo da chi deve effettivamente inviare dati (assegnazione dinamica).
Nessuna stazione gestisce il canale, ma tutte le stazioni lo devono contendere.
Due possibili modalità di **tempo di trasmissione:**
- Tempo continuo: la trasmissione può iniziare in qualunque istante.
- Slotted: Il tempo è diviso in intervalli detti Slot, la trasmissione deve coincidere con l'inizio di un intervallo.

Attenzione alle **collisioni:** l'accesso a contesa implica che un frame potrebbe entrare in collisione con un altro, in questo caso entrambi dovranno essere inviati nuovamente.
Un protocollo che gestisce i tempi di trasmissione e le eventuali collisioni è detto ad <mark style="background: #946EFA;">Accesso Multiplo - MA.</mark>

Come faccio a verificare l'occupazione del canale? Le stazioni verificano lo stato del canale prima di decidere se iniziare la trasmissione **Carrier Sense - CS**, mentre alcuni protocolli verificano lo stato del canale anche durante la trasmissione per individuare rapidamente eventuali collisioni **Collision Detection - CD**.

Vediamo quindi alcuni protocolli ad Accesso Multiplo:

## ALOHA
Ogni terminale invia i frame senza accordo con gli altri; se due o più stazioni trasmettono contemporaneamente e i loro segnali si sovrappongono, si verifica una collisione. Quando una stazione rileva una collisione o non riceve una conferma, considera che la sua trasmissione non è andata a buon fine.
In caso di collisione parte un algoritmo chiamato **Backoff** che determina un tempo di attesa prima di riprovare, quello più usato è <mark style="background: #946EFA;">l'esponenziale binario:</mark>
Dopo n collisioni consecutive si attende un numero di slot random tra 0 e 2N -1, per esempio Ethernet ammette un valore massimo di n=10.
Dopo la prima collisione l'invio può avvenire dopo 0 slot (subito) con prob. 50%
oppure dopo una attesa di 1 slot con prob. 50%.
Dopo la seconda collisione la trasmissione avviene con probabilità al 25% per i 4 casi (0,1,2,3), e così via.

>Nota: Se un host spedisce un frame in un determinato slot, la probabilità di avere un collisione è data dalla somma delle probabilità di trasmissione degli altri host meno la probabilità del loro verificarsi in contemporanea (per non contarli doppi).

- ALHOA PURO: è uno dei primi protocolli di accesso al mezzo trasmissivo per reti di computer e viene utilizzato per il trasferimento di pacchetti di dati attraverso un canale condiviso, esso non evita completamente le collisioni ma cerca di gestirle in modo efficiente.
  Frame-Time T è il tempo necessario per trasmettere un frame, essi hanno lunghezza costante di L bits: $$ T = L/bitRate $$
   Nel momento della collisione anche con una sovrapposizione di un singolo bit entrambi i frame sono danneggiati; l'intervallo di tempo in cui si può avere una collisione, chiamato **Tempo di Vulnerabilità**, è di 2T.
   Con N frame generati nel tempo T:
	- se 0 < N < 1 ci aspettiamo un throughput ragionevole
	- se N > 1 si va direttamente alla paralisi
  Per ogni collisione è necessario rispedire il frame, se G è il carico generato nel tempo T abbiamo: $$ G = N + frameRispediti$$
- Slotted ALOHA: Un altro tipo di protocollo per gestire le collisioni, più recente.
  Il tempo viene diviso in intervalli discreti, le trasmissioni possono iniziare solo all'inizio di un intervallo; una speciale stazione emette un segnale all'inizio di ogni intervallo per sincronizzare i trasmettitori.
  Il **tempo di vulnerabilità** è dimezzato rispetto a Pure ALOHA.

Il carico *G* si riferisce alla quantità di dati trasmessi durante un certo intervallo di tempo *T*, la probabilità *P* si riferisce alla probabilità che una stazione trasmessa abbia successo nel tempo di vulnerabilità *T*. Nel contesto di ALOHA puro, questa è la probabilità che una stazione trasmetta un pacchetto e non si verifichino collisioni.
La capacità di trasporto *S* (o throughput) è la quantità di dati effettivamente consegnati con successo attraverso il canale in un certo periodo di tempo. Può essere calcolata come: $$ S= G*P[0] $$
Questo significa che il throughput *S* è direttamente proporzionale al tasso di trasmissione delle stazioni *G* e alla probabilità di successo*P*, in altre parole, se aumenti il tasso di trasmissione *G* o migliori la probabilità di successo *P*​, il throughput *S* aumenterà.​
La probabilità di generare *k* frame durante un certo intervallo di tempo *T* è dato dalla <mark style="background: #946EFA;">distribuzione di Poisson: </mark>
$$ P[k] = \frac{G^k*e^{-G}}{k!} $$
dove:
*P(k)* = rappresenta la probabilità di generare *k* frame.
*G^k* = è il tasso di trasmissione delle stazioni elevato alla k-esima potenza.
e^(-G) = è la funzione esponenziale di *G* elevato a meno uno.
*k!* = rappresenta il fattoriale di *k*

---

<span style="color: #946EFA;">Esempio:</span>
**ALOHA puro**
Per un periodo di vulnerabilità pari a 2T la probabilità che nessun altro frame venga generato durante il periodo di vulnerabilità:

$$P[0] = \frac{G^0 * e^{-2G}}{0!} = e^{-2G}$$
Throughput per *G* = 0.5:
$$ S = G*e^{-2G} = 0.36 $$

**Slotted ALOHA**
Il tempo di vulnerabilità è T (dimezzato rispetto a Pure Aloha), quindi:
$$P[0] = \frac{G^0 * e^{-G}}{0!} = e^{-G}$$
Throughput per *G* = 1:
$$ S = G*e^{-G} = 0.36 $$

---

## CSMA (Carrier Sense Multiple Access)
Migliora le prestazioni, rispetto ad ALOHA, aggiungendo l’ascolto del canale, se il canale è occupato pospone la trasmissione; il numero di collisione è molto ridotto (ma non azzerato):
$$ G ≈ N $$
**CSMA non persistente**
Se il canale è libero inizia la trasmissione altrimenti attende un tempo casuale prima di ritentare (anche in assenza di collisioni). Diminuisce la probabilità di collisione poiché è improbabile che 2 stazioni aspettino lo stesso tempo, ma aumenta il ritardo di trasmissione (anche in una rete con poco traffico).

**CSMA 1-persistente**
Se il canale è libero inizia la trasmissione altrimenti attende che si liberi prima di ritentare.
E' detto 1-persistente perché trasmette con probabilità 1 quando il canale è libero.
Problema: in caso di alto traffico è probabile che 2 nodi in attesa entrino in collisione.

**CSMA p-persistente**
Si applica ai canali divisi in intervalli temporali, **se il canale è libero** la trasmissione avviene con probabilità p e viene rimandata all’intervallo successivo con probabilità 1-p, se anche questo è libero la trasmissione avviene con probabilità p e così via.
**Se il canale è occupato** si comporta come se ci fosse stata una collisione: parte un algoritmo di Backoff (generalmente l'attesa è proporzionale al numero di collisioni consecutive), al crescere di p diminuisce il ritardo, ma aumenta la probabilità di collisione.

## CSMA/CD (Carrier Sense Multiple Access - Collision Detect)
Chi spedisce rimane in ascolto sul canale anche durante la trasmissione.
Vantaggi:
- in caso di collisione si interrompe la trasmissione → si riduce il tempo di vulnerabilità
- il mittente capisce se il Frame è stato inviato correttamente (senza collisioni)
Se *Tpr* è il tempo di propagazione del cavo, il massimo ritardo nell’individuare una collisione è *2Tpr* (supponendo che il secondo nodo all’altro estremo inizi la trasmissione un attimo prima di ricevere il pacchetto)
Per individuare con certezza una collisione è quindi necessario che il frame abbia
un tempo di trasmissione: $$ T_{tr} >= 2T_{pr} $$
L'insieme dei nodi che concorrono per accedere allo stesso mezzo trasmissivo
costituisce un **Dominio di Collisione** (Collision Domain).
Il **Dominio di Broadcast** è l'insieme dei nodi che possono comunicare direttamente,
senza dover risalire al livello rete.
I due domini possono non coincidere per effetto di apparati di rete (Bridge) che separano i domini di collisione ma non i domini di broadcast.

## LAN Wireless Protocolli
Nelle reti Wireless il dominio di collisione non è nettamente definito come nelle reti wired, in quelle wireless, il concetto di dominio di collisione è meno rilevante. In una rete wireless, i dati vengono trasmessi attraverso onde radio e non ci sono cavi fisici, di conseguenza, i dispositivi non competono fisicamente per lo stesso "spazio di trasmissione" come farebbero in una rete cablata.
Invece, le collisioni possono ancora verificarsi, ma sono gestite tramite tecniche di accesso al mezzo come il CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance).

---

**Esempi:**

**Problema del nodo nascosto:** B trasmette a C,  D non sente il segnale di B e trasmette contemporaneamente a B creando collisione non rilevata da B.

**Problema del nodo esposto:** B trasmette ad A, C vorrebbe trasmettere a D ma non lo fa perché crede erroneamente di creare una collisione.

![[Wireless.svg]]

---

## CSMA/CA (Collision Avoidance)
Prima di trasmettere, una stazione wireless ascolta il canale per verificare se è già in uso da altre stazioni. Se il canale è occupato, la stazione attende prima di tentare di trasmettere.
Se il canale sembra libero dopo l'ascolto, la stazione che desidera trasmettere invia un piccolo pacchetto chiamato "Richiesta di Trasmissione" (RTS) al destinatario. L'RTS indica quanto tempo la stazione intende occupare il canale.
Il destinatario risponde con un messaggio "Conferma di Trasmissione" (CTS) per confermare che è pronto a ricevere i dati. Il CTS contiene informazioni sulla durata della trasmissione, dopo di che la stazione trasmette i dati al destinatario.