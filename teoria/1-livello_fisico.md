```table-of-contents
```
---

# Livello Fisico

Il <mark style="background: #946EFA">Livello Fisico</mark> riceve dal livello superiore (Collegamento) i frame da trasmettere, li converte in una sequenza di bit, tramite un *adattatore*, e li riversa sul canale in cui troverà altri nodi collegati, a questo punto i bit verranno poi decodificati, tramite un *adattatore*, dal livello fisico del nodo destinatario.
Il collegamento tra nodi, come abbiamo visto in precedenza, può essere effettuato in due modalità: Punto a Punto o Multi-Accesso.
Il trasferimento avviene utilizzando un **Mezzo Trasmissivo** su cui i bit vengono codificati trasformandoli in una forma di energia (luce, tensione, onde, ecc.).

# Tipi di mezzi trasmissivi
- **Elettrico**
	- Cavi coassiali in rame (multi-accesso)
	- Doppini telefonici (punto a punto)
- **Ottico**
	- fibre ottiche (punto a punto)
- **Wireless**
	- onde radio omnidirezionali (multi-accesso)
	- ponti radio (punto a punto)
	- satelliti (punto a punto o multiaccesso)

---

**Vediamo alcune <mark style="background: #946EFA;">caratteristiche</mark> per cui bisogna tenere conto per la scelta del mezzo trasmissivo:**

## Banda Passante (Hz)
E' una banda che, contenente intervalli di frequenze, viene utilizzata per la codifica dei dati, in cui l'[[#Attenuazione (dB)]] tende ad essere **più bassa e costante possibile**.
Solitamente la banda passante (larghezza) è determinata dal mezzo fisico che scegliamo di utilizzare, ma possiamo anche limitarla artificialmente tramite *filtri passa banda*.
<mark style="background: #946EFA;">Le onde</mark> vengono misurate in base alla loro frequenza f (Hz) o lunghezza λ (metri), il prodotto di queste due grandezze definiscono la <mark style="background: #946EFA;">velocità di propagazione v.</mark>
$$ v = λ * f $$

## Attenuazione (dB)
Il segnale durante il percorso all'interno del mezzo trasmissivo può diminuire, è possibile quindi determinare la massima distanza raggiungibile attraverso una formula.
$$MaxDist = 10*Log(P2/P1)$$
dove: 
P1 = Trasmittente.
P2 = Ricevente.

## Distorsione
Se la banda passante utilizzata non ha valori costanti di attenuazione, come abbiamo ipotizzato precedentemente, si deve aggiungere il fenomeno della distorsione che è quindi dovuto alla maggiore attenuazione di alcune frequenze, solitamente si parla di quelle più alte.

## Rumore (dB)
Al segnale che passiamo all'interno della banda, con potenza S, si sovrappone anche il Rumore termico che, con potenza N, è dovuto al movimento delle molecole del mezzo.
Il rapporto segnale/rumore (SNR - Signal Noise Ratio) viene calcolato:
$$SNR = 10*Log(S/N)$$
## Disturbo
Proviene da fonti esterni.

---

# Velocità massima di trasmissione di un canale
Per  <mark style="background: #946EFA;">Banda passante analogica</mark> si intende il range di frequenze in cui un sistema può trasmettere o ricevere segnali analogici, cioè segnali che vengono rappresentati attraverso delle onde e quindi misurati in Hz.
Quando si parla di  <mark style="background: #946EFA;">Ampiezza di banda digitale</mark>, si indica la quantità di segnali digitali, cioè segnali rappresentabili in forma binaria, che possono essere trasmessi attraverso un canale di comunicazione in un dato periodo di tempo, deduciamo quindi che l'unità di misura sarà bit/sec.
Possiamo dunque stabilire una relazione tra questi due concetti, basandoci sul teorema di  <mark style="background: #946EFA;">Shannon-Nyquist.</mark>

>**Teorema Shannon-Nyquist**
>Stabilisce una relazione tra: la frequenza di campionamento di un segnale analogico e la massima frequenza che può essere rappresentata accuratamente nel processo di campionamento.
>Formulazione classica del teorema: per rappresentare correttamente un segnale analogico con frequenza massima B in Hz, è necessario campionare a una frequenza di almeno 2B campioni al secondo.
>Spiegandoci in poche parole, se desideri ***digitalizzare un segnale analogico*** senza perdere informazioni importanti, devi campionare a una frequenza che è almeno il doppio della frequenza massima presente nel segnale analogico.

Possiamo dire che la velocità massima (in bit al secondo) a cui è possibile trasmettere attraverso un canale con una banda passante (in Hertz) è data da:
$$
B = 2H*Log_2(V)
$$
dove:
- B = l'ampiezza di banda digitale (bit/sec)
- H = la banda passante analogica (Hz)
- V = numero di simboli del segnale

In presenza di ***rumore*** il teorema Shannon-Nyquest può essere esteso per considerare anche il rapporto segnale-rumore (SNR), infatti, il <mark style="background: #946EFA;">teorema di Shannon-Hartley</mark> è una versione più completa.
$$
B = H*Log_2(1+S/N)
$$
dove:
- B = l'ampiezza di banda digitale (bit/sec)
- H = la banda passante analogica (Hz)
- S = potenza del segnale
- N = potenza del rumore

## Esercizio
*In un canale con Banda passante analogica (H) = 3KHz e un rapporto segnale-rumore (S/N) = 30dB, calcolare l'ampiezza di banda digitale.*

H = 3KHz = 3000Hz

Dato che il rapporto segnale-rumore è dato in dB, cioè rappresentato su scala logaritmica, dobbiamo trasformarlo in scala lineare, quindi applichiamo la seguente formula generica per la trasformazione:
$$
x_{lineare} = 10^{(x_{logaritmico}/10)}
$$
Quindi troviamo:
$$
S/N = 10^{(30/10)} = 1000
$$
Applichiamo la formula del teorema di Shannon-Hartley: 
$$ B = H*Log_2(1+S/N) = 3000*Log_2(1+1000) ≈ 30Kb/s$$
*Ora voglio calcolare il numero di simboli ottimali.*

Applichiamo la formula inversa del teorema Shannon-Nyquest:
$$ V = 2^{(B/2H)} = 2^{(30/6)} = 32 $$

---

# Tempi

## Tempo di consegna
E' il tempo necessario per trasferire un messaggio (sequenza di bit) dal mittente al destinatario ed è determinato dalla somma di diverse latenze introdotte dal mittente, dai nodi di transito, dal mezzo trasmissivo e dal destinatario.
## Il Round Trip Time (RTT)
E' il tempo che intercorre tra l'invio di un dato e la ricezione di un messaggio di riscontro.

## Tempo di trasmissione (bit/sec)
E' il tempo necessario per inviare un certo numero di bit attraverso il mezzo di comunicazione fisico a una certa velocità di trasmissione. Questo tempo può variare in base al tipo di mezzo di trasmissione utilizzato, alla sua larghezza di banda e dal numero di bit.

$$ TempoDiTrasmission = nDiBit/velocitàDiTrasmissione $$

## Tempo di propagazione
Indica il tempo impiegato da un bit per viaggiare da un punto all'altro nel mezzo di trasmissione.
$$TempoDiPropagazione = LunghezzaMezzo/VelocitàPropagazioneNelMezzo$$

## Tempo di preparazione del mittente
Tempo necessario al mittente per la preparazione del dato da spedire (ad esempio tempi di codifica e compressione).

## Tempo di riempimento del pacchetto (Real Time Streaming)
Nel contesto dello streaming si riferisce al periodo di tempo necessario per compilare un pacchetto di dati con un volume sufficiente di informazioni per essere trasmesso attraverso la rete. Questo concetto è particolarmente rilevante in applicazioni di streaming in tempo reale come la trasmissione video o audio.

Per esempio, quando stai guardando un video in streaming in tempo reale, l'immagine e il suono vengono divisi in piccoli pacchetti di dati. Ogni pacchetto deve contenere un numero sufficiente di informazioni in modo che, una volta ricevuto dal dispositivo del destinatario, possa essere riprodotto senza interruzioni o ritardi.

## Tempo di elaborazione (o inoltro)
Si riferisce al periodo di tempo che un nodo di transito impiega per processare e inoltrare un pacchetto di dati che transita attraverso di esso.

## Tempo di attesa
Se un nodo di transito utilizza delle code di trasmissione, si deve introdurre un tempo di attesa necessario per lo smaltimento della coda.

## Tempo di elaborazione del destinatario
Tempo che viene impiegato per la decodifica e la decompressione dell'informazione ricevuta.

---

# Modi per trasmettere

**Cavo in Rame**
E’ un mezzo trasmissivo a basso costo; l’attenuazione del segnale cresce rapidamente con la frequenza e con la distanza, per questo motivo è largamente utilizzato nelle reti locali.
Esistono 2 principali tipi di cavi:
- **Cavo coassiale** 
	Due cavi di rame concentrici e separati da un materiale isolante.
	La parte esterna è realizzata con una calza di conduttori sottili.
	Solitamente utilizzato come canale Multiaccesso e Half-duplex, poco utilizzato
- **Doppino**
	Coppia di fili di rame avvolti non schermati (UTP - Unshielded Twisted Pair).
	Viene realizzato con diversi standard qualitativi a seconda del tipo di utilizzo.

**Fibra Ottica**
Fibre di vetro che trasportano impulsi di luce su fibre flessibili del diametro di qualche decina di micron (1 micron = 10-6m).
- Ottimo rapporto Segnale/Rumore (60 – 65 dB).
-  Elevata banda trasmissiva (25000-30000 GHz, fino a 50 Tbps)
 - Bassa attenuazione
 - E’ immune da disturbi elettromagnetiche
 - Sicurezza (difficile inserirsi in una comunicazione)
 - Minor dimensione e peso rispetto al rame
 - Maggior costo di installazione, connessione e dei dispositivi attivi.

**Trasmissione ottica**
Si hanno una o più bande dove l'attenuazione è costante e quindi posso passare il segnale.

**Onde elettromagnetiche**
Le onde e.m. possono essere utilizzate per trasmettere informazioni senza l’utilizzo di un mezzo fisico guidato.
La trasmissione dei dati avviene modulando una frequenza portante (carrier), come avviene per le trasmissioni radio AM o FM (Modulazione di Ampiezza o di Frequenza)
Per trasmissione dati viene modulata l’ampiezza, la frequenza o la fase delle onde di una portante, ma codificando valori discreti.

Al crescere della frequenza aumenta l'ampiezza del canale, ma peggiora l'interazione con l'ambiente.
Un esempio comune riguarda le trasmissioni radio, aumentando la frequenza del segnale, si può ottenere una maggiore larghezza di banda disponibile per la trasmissione di dati. Tuttavia, a frequenze più elevate, il segnale tende ad essere più suscettibile a interferenze e attenuazioni causate da elementi dell'ambiente circostante, come edifici, ostacoli naturali o altre fonti di interferenza elettronica.

---

## Modulazione digitale
E' il processo di conversione dei dati digitali in segnali digitali che possono essere voltaggi, intensità di luce, o segnali elettromagnetici, secondo le caratteristiche della linea di comunicazione usata per il collegamento. Questa tecnica è chiamata codifica.

## Tecniche di trasmissione

**Trasmissione in banda base**
In questo caso il segnale viene trasmesso direttamente senza modulazione, utilizzando la frequenza naturale, ciò significa che il segnale occupa una frequenza di banda molto stretta intorno a zero Hertz, quindi si utilizzano per la rappresentazione onde quadre.
La trasmissione in banda base è comunemente utilizzata in sistemi di comunicazione a corto raggio, come comunicazioni LAN (Local Area Network) e collegamenti tra dispositivi all'interno di un edificio.

>*Svantaggi: La trasmissione in banda base può essere limitata in termini di portata e suscettibile  a disturbi e interferenze.*

**Trasmissione in banda passante**
In questo caso il segnale viene modulato su una portante, creando un segnale con una frequenza più alta e una larghezza di banda maggiore rispetto al segnale originale, ciò significa che il segnale occupa una gamma più ampia di frequenze rispetto a una trasmissione in banda base e quindi viene utilizzata per la rappresentazione un'onda sinusoidale, detta *portante*.
La trasmissione in banda passante è comunemente utilizzata in comunicazioni a lunga distanza, come la trasmissione radio, televisiva e le reti cellulari.

>*Vantaggi: La trasmissione in banda passante può coprire lunghe distanze e superare ostacoli, ed è in grado di gestire un maggior numero di canali simultanei rispetto alla trasmissione in banda base.*

Il trasferimento dei bit avviene codificando su due o più simboli, il **numero di simboli** trasmessi in un secondo è detto <mark style="background: #946EFA;"> Baud-rate.</mark>
I simboli vengono codificati all'interno di intervalli di tempo costante (**Clock**) che rappresentano il sincronismo condiviso tra trasmettitore e ricevitore.

## Modalità di trasmissione

**Modalità Asincrona**
Ogni gruppo di bit è inviato in modo <mark style="background: #946EFA;">asincrono</mark> (è possibile l'assenza di segnale tra un gruppo e il successivo); ogni gruppo è preceduto da una sequenza di bit aggiuntivi che consentono al destinatario di ricostruire il sincronismo.
Questa è la modalità utilizzata nelle reti calcolatori.

**Modalità Sincrona**
E' un metodo di trasferimento di dati in cui il flusso di segnali di dati è continuo ed è accompagnato da segnali di temporizzazione. Aiuta a garantire che il trasmettitore e il ricevitore siano sincronizzati tra loro.
Generalmente questo è possibile solo per connessioni a breve distanza e alta velocità.

## Schemi di codifica di linea
Possiamo avere diversi modi per schematizzare la codifica dei dati, essi vengono utilizzati nella PCM (trasmissione telefonica digitale):
- Return to Zero (RZ): solitamente è più soggetto ad errori, ma non perde il sincronismo; un bit 1 viene rappresentato da un cambiamento di stato nel segnale durante il periodo di simbolo, mentre un bit 0 viene rappresentato da nessun cambiamento di stato.
- Not Return to Zero (NRZ): E' meno frequente agli errori, ma la quantità di di zeri e uni potrebbero causare perdita di sincronismo.

![[RZ_NRZ.svg]]

- Not Return to Zero Inverted (NRZ-I): cambia il simbolo di codifica quando incontra il bit 1.
- Manchester: codifica i bit con le transizioni (quando incontro 1 mi abbasso, 0 mi alzo).
- Manchester differenziale: combina la codifica Manchester con la NRZ-I (1 cambia il simbolo di codifica, 0 lo mantiene).

![[Manchester.svg]]
## Quadrature Amplitude Modulation (QAM)
La più efficiente e usata modulazione è la QMA e si tratta della modulazione di ampiezza e fase; ogni simbolo è determinato da una coppia di essi (fase-ampiezza) e viene rappresentato da un punto nel diagramma delle fasi, l'insieme dei punti formano una costellazione.

![[QMA.svg]]
## Multiplexing
Quando la larghezza di banda del canale trasmissivo è maggiore della larghezza di banda effettivamente necessaria, il canale può essere condiviso da più trasmissioni simultanee.
Il Multiplexing è la tecnica che permette la trasmissione simultanea di più segnali in un singolo canale.
Esistono diverse tecniche di per implementare il multiplexing, le principali sono:
- A divisione di frequenza **FDM** (analogico)
	Divide lo spettro in bande di frequenza, ogni canale viene codificato modulando le frequenze all’interno di una banda.
- A divisione di tempo **TDM**
	E' tipico delle trasmissioni digitali. Il tempo viene diviso in frame di dimensione stabilita, ogni frame ospita un numero definito di canali.
	I dati di un linea di input vengono inseriti nel canale assegnato.
- **OFDM (Orthogonal Frequency Division Multiplexing)** 
	E' una tecnica FDM in cui le frequenze portanti sono tra loro ortogonali e viene utilizzata nelle principali tecnologie per trasmissione dati quali ADSL, WiFi 802.11g e 802.11n, WiMAX e nei sistemi cellulari LTE.

---

# Il sistema telefonico
Il sistema telefonico (PSTN - Public Switched Telephone Network) è una rete specializzata per la trasmissione di uno specifico tipo di dato: <mark style="background: #946EFA;"> la voce analogica.</mark>

**Fino agli anni 60**
Ogni telefonata richiedeva una banda analogica di 4KHz tra l’utente e la centralina telefonica su un doppino telefonico in rame detto Ultimo Miglio (o Local Loop).
All'interno dell'azienda Telecom per consentire il trasporto di più conversazioni telefoniche su un unico canale utilizzava la tecnica di multiplexing FDM (vista precedentemente), cioè veniva suddivisa la banda di frequenza in diverse fasce più strette, di almeno 4KHz, ognuna delle quali è utilizzata per trasmettere un segnale indipendente.

**A partire dagli anni 60**
Le comunicazioni audio vengono gestite in modo digitale dalle compagnie telefoniche.
La conversione digitale è standardizzata con la tecnica di campionamento **PCM (Pulse Code Modulation)**, *come funziona?*
Il segnale analogico (come quello proveniente da una chiamata telefonica) viene campionato periodicamente. Questo significa che, a intervalli regolari di tempo, viene preso un campione del segnale analogico, successivamente ogni campione viene convertito in un valore digitale, generalmente con l'uso di un quantizzatore. Questo processo comporta l'assegnazione di un valore numerico discreto a ciascun campione in base a una scala di quantizzazione predefinita.
I valori digitali ottenuti dal processo di quantizzazione vengono quindi codificati in un formato specifico, <mark style="background: #946EFA;">PCM</mark>, comunemente si utilizza una rappresentazione binaria per i valori quantizzati, i dati digitali così ottenuti possono essere trasmessi attraverso reti di comunicazione digitali.
Nel ricevitore, il processo viene invertito, il segnale ricostruito viene convertito nuovamente in un formato analogico, in prossimità della destinazione, utilizzando un dispositivo chiamato Codec (coder-decoder).
In questo caso il multiplexing delle portanti avviene in Time Division Multiplexing (TDM, visto precedentemente), ovvero suddividendo il tempo del canale in slot che si ripetono ciclicamente.

---
<p style="color: #946EFA;">Esempio:</p>
Il canale analogico ha una larghezza di banda di 4 kHz, per rappresentare correttamente un segnale analogico su un sistema digitale, è necessario campionare il segnale a una frequenza almeno doppia della frequenza massima del segnale (teorema di Nyquist-Shannon). 
Nel nostro caso del canale con banda di 4 kHz, la frequenza di campionamento deve essere di almeno 8.000 campioni al secondo (Hz) per rappresentare adeguatamente il segnale analogico.
Ogni campione viene rappresentato utilizzando 8 bit di dati (scelta comune nella quantizzazione e campionamento PCM), quindi per calcolare il flusso di dati, moltiplichiamo la frequenza di campionamento per il numero di bit utilizzati per rappresentare ciascun campione: 

$$ 8.000 cam/sec * 8 bit = 64.000 bit/sec = 64 Kb/s $$

---

# Digitalizzazione dell'ultimo miglio
Abbiamo bisogno di modulare i bit con segnali analogici assimilabili alla voce umana, inviarli nel sistema telefonico e demodularli in digitale dalla parte del ricevente, tutto ciò è possibile attraverso il **Modem**, il quale avendo a disposizione un canale di 4KHz può trasmettere fino a 56 Kb/s.
Con la tecnologia **ISDN** è stato possibile propagare il segnale digitale anche sull’ultimo miglio, portando in casa dell’utente un canale digitale da 64Kb/s.
Negli anni 2000 per aumentare la velocità è stato introdotta la tecnologia **xDSL** che sfrutta la maggiore banda di frequenze dei cavi in categoria 3.

>Vantaggi:
>- Il segnale domestico non viene filtrato a 4 KHz ma a **1.1MHz**
>- La banda viene suddivisa in 256 canali da **4.3KHz** (1.1 MHz / 256 canali) con tecnica OFDM.
>- All'interno di ogni canale si usa la modulazione QAM con un rate di 4K baud.
>- La qualità della linea viene costantemente monitorata per aggiustare la velocità di trasmissione, utilizzando costellazioni con più o meno punti.
>- Massimo numero di bit per baud è 15 (32768-QAM)
>- Massima velocità di un canale **60 Kb/s** (4K baud * 15 bit per baud)
>- Massima velocità aggregata è quindi ~ **15 Mb/s** (60 Kb/s * 256 canali)

**ADSL (Asymmetric DSL)** è un utilizzo specifico di xDSL, pensato per l'home computing, in cui il download è prevalente.
**ADSL2** migliora le prestazioni attraverso una diversa codifica con una maggiore efficienza.
**ADSL2+** e un nuovo standard che utilizza una banda doppia.
L'ultimo miglio in rame limita le prestazioni di ADSL, le compagnie telefoniche stanno sostituendo il rame con fibre ottiche che arrivano in prossimità dell'abitazione o in casa.
FttC (Fiber to the Cabinet, ovvero l'armadio in strada) può arrivare ad una banda di 35Mhz e una velocità di 300 Mb/s.
FttH (Fiber to the Home) arriva a 1 Gb/s.
Queste tecnologie vengono genericamente riferite come FttX.

