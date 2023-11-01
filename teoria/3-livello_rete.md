```table-of-contents
```
---

# Livello Network
Questo livello si occupa di instradare i pacchetti di dati dal mittente al destinatario attraverso una serie di dispositivi di rete come router. Utilizza indirizzi IP per identificare i dispositivi di origine e destinazione nella rete e prende decisioni sul percorso ottimale per la trasmissione dei dati. Inoltre, gestisce questioni di congestione, controllo di flusso e può offrire servizi di qualità del servizio (QoS) per ottimizzare la prestazione della rete.
La **commutazione**, o switching, è una tecnica che permette di instradare i pacchetti di dati in modo efficiente tra i dispositivi connessi, le due tecniche usate principalmente per la commutazione sono:
- **Commutazione di circuito** (utilizzata solitamente dai provider di telefonia)
- **Commutazione di pacchetto** (utilizzata nelle reti di calcolatori)

---
## Commutazione di circuito
I nodi di transito, che possono essere centralini di commutazione manuali, meccanici o elettronici, svolgono un ruolo cruciale nel processo di instradamento delle comunicazioni.
Durante la fase di connessione, vengono assegnate e allocate le risorse necessarie per garantire una comunicazione fluida. Tuttavia, è importante notare che, sebbene il trasferimento dei dati avvenga con un ritardo minimo, il tempo richiesto per aprire e chiudere la connessione può risultare relativamente lungo.
Un aspetto interessante da considerare è l'efficienza nell'uso delle risorse. Nel caso delle telefonate, le risorse vengono allocate solo durante la chiamata stessa e rilasciate al termine. Tuttavia, per il trasferimento di dati, le risorse vengono riservate anche se la connessione rimane inutilizzata per un periodo di tempo, il che può comportare uno spreco di capacità.

---
## Commutazione di pacchetto
Immagina di inviare un messaggio attraverso una rete di comunicazione. Piuttosto che inviarlo come un flusso continuo, viene suddiviso in piccoli <mark style="background: #946EFA;">pacchetti</mark> di dati. Ogni pacchetto è come una porzione del messaggio che può viaggiare autonomamente attraverso la rete.
Ogni volta che un pacchetto si muove, un algoritmo nel sistema di rete prende decisioni su come instradarlo. Questo significa che l'attenzione si concentra sui pacchetti individuali, non sull'intero flusso del messaggio.
Nel mondo della rete, ci sono diversi tipi di dispositivi che gestiscono questi pacchetti in base alle loro funzioni. Ci sono **hub**, **bridge**, **switch**, **router** e **gateway**, ognuno con un ruolo specifico nella trasmissione dei dati.
C'è anche una distinzione importante tra due tipi di commutazione a pacchetto: 
- **a circuito virtuale**, dove viene stabilito un percorso predeterminato per i pacchetti. 
- **a datagramma**, dove ogni pacchetto viene instradato in modo indipendente in base alle condizioni della rete in quel momento.
Questa architettura di comunicazione frammentata in pacchetti offre notevoli vantaggi, inclusa una maggiore affidabilità e flessibilità nella gestione del traffico di dati attraverso le reti.

### Commutazione di pacchetto a circuito virtuale
Nella commutazione a circuito virtuale, un percorso predeterminato è stabilito all'apertura del Canale Virtuale (VC). Ad ogni VC è assegnata un'etichetta che guida il percorso, ogni router lungo il percorso viene contrassegnato con l'etichetta del VC e l'indicazione della porta di uscita associata. 
È ampiamente usato nelle reti ATM per la telefonia e in Internet tramite il protocollo [[#MPLS - MultiProtocol Label Switching]].
Va notato che la **versione 6 del protocollo IP**, noto come IPv6, supporta anche reti a circuito virtuale, aggiungendo ulteriori opzioni e flessibilità nell'architettura delle comunicazioni.

*Questo dimostra quanto la commutazione a circuito virtuale sia una componente vitale nella progettazione e nell'ottimizzazione delle reti di comunicazione moderne.*

#### MPLS - MultiProtocol Label Switching
MPLS consente di creare in Internet aree a commutazione di Label (etichette), come funziona? 
Il router frontiera (Edge) assegna **un etichetta** ai pacchetti (header MPLS), permettendo ai router di prendere decisioni di instradamento basate su queste etichette anziché analizzare l'indirizzo IP completo, attraverso questi label il primo pacchetto definisce un *tunnel* nella rete dove i pacchetti successivi della stessa connessione seguono il percorso del primo pacchetto. 
Questo garantisce una coerenza nel percorso seguito dai pacchetti di una specifica connessione, contribuendo alla stabilità e alla coerenza delle comunicazioni, è ampiamente usato in reti di telecomunicazioni e data center per migliorare le prestazioni.

---

### Commutazione di pacchetto a datagramma
Nella commutazione a datagramma, i pacchetti viaggiano indipendentemente basandosi sull'indirizzo di destinazione. L'instradamento è deciso da tabelle costruite dinamicamente da ogni router, utilizzando algoritmi di routing. 
Pacchetti della stessa connessione possono seguire percorsi diversi, questo approccio è <mark style="background: #946EFA;">fondamentale in implementazioni come IPv4 e IPv6.</mark>

### Routing
Il routing è quella parte del software dello strato Network che si preoccupa dell'instradamento dei pacchetti in transito.
Se la **Rete è a Datagramma** il routing viene determinato per ogni pacchetto, poiché il percorso migliore può cambiare nel tempo.
Se la **Rete è a Circuito Virtuale** il routing viene determinato al momento dell'attivazione del circuito, da quel momento in poi tutti i pacchetti seguono il percorso stabilito.

---

### Protocolli TCP/IP
Ogni strato al di sotto di IP è specifico della singola sottorete e non richiede particolari dettagli. IP si occupa di funzioni di rete e dell'instradamento dei pacchetti. TCP (o UDP) gestisce il trasporto e il controllo della connessione da un'estremità all'altra. Lo strato di applicazione ospita i software utilizzati per offrire servizi direttamente agli utenti.

---
## Standard di Internet
Non esistono organizzazioni o enti centrali che gestiscono l'intera Internet in modo diretto, invece, ci sono enti che coordinano le attività di ricerca e sviluppo relative alla rete. 
Attualmente, molte di queste funzioni di coordinamento sono riunite sotto <mark style="background: #946EFA;">l'Internet Society</mark>, un'organizzazione globale senza scopo di lucro che promuove lo sviluppo e l'uso aperto dell'Internet.
Dalla **IS** dipende l'**Internet Advisory Board** (IAB), ente che si occupa dei protocolli internet, e si compone di due sottogruppi:
- **Internet Research Task Force (IRTF):** coordina le attività di ricerca.
- **Internet Engineering Task Force (IETF):** coordina le attività di ingegnerizzazione ed implementazione, IETF pubblica nei RFC (Request For Comment).

## IP - Internet Protocol
Come funziona?
Lo strato di trasporto prende il flusso di dati e li divide in **datagrammi** che passa allo
strato IP, la dimensione massima è di 64KB, ma generalmente vengono scelti datagrammi non superiori a 1500 Byte (per compatibilità con Ethernet).
Il datagramma di trasporto (detto Segmento) viene incorporato nella **trama IP**, cioè nella struttura del pacchetto, e trasferito da un router all’altro fino a destinazione.
Il datagramma può subire una **frammentazione** nel caso di passaggio attraverso un
livello data-link con dimensione massima (MTU) inferiore, i frammenti vengono riassemblati a destinazione.
Il datagramma (eventualmente riassemblato) viene estratto dalla **trama IP** e passato al livello di trasporto, che **ricostruisce il flusso.**
**QoS**: La consegna è di tipo **Best Effort**, indica che la rete farà del suo meglio per trasmettere i dati, ma non può garantire specifici livelli di qualità o prestazioni. In questo caso, la consegna dei pacchetti avviene senza particolari garanzie o prioritizzazioni.

>  *QoS, acronimo di Quality of Service, è un insieme di tecnologie e meccanismi che mirano a migliorare la qualità e l'affidabilità della trasmissione dei dati attraverso una rete.*

---
### Struttura della trama IP
Il datagramma IP è costituito dall’intestazione (header) IP seguita dal segmento del
livello di trasporto, l’header ha una parte fissa e una parte opzionale variabile e viene trasmessa in ordine big endian.

![[header-ip.png]]

- **Version (4 bit):** i primi 4 bit di ogni pacchetto IP contengono il numero di versione.
- **IHL (4 bit) :** dimensione dell’header espressa in parole di 4 byte (da 5 a 15)
- **Type of Service (6 bit):** 
	- Inizialmente per controllo della rete (priorità e segnalazioni).
	- Con l'RFC 2474 diventa Servizi Differenziati per la codifica delle Classi di Servizio.
	- In realtà Internet è “best effort”: questo campo è quasi sempre inutilizzato.
- **Total Lenght (16 bit):** Numero di byte totali header+dati (fino a 64K)
- **Identification (16 bit):** Tutti i frammenti di datagramma hanno lo stesso valore
- **DF (1 bit):** Don’t Fragment → ordina ai router di non frammentare
- **MF (1 bit):** More Fragments → 1 per tutti i frammenti tranne l’ultimo
- **Fragment Offset (13 bit):** Indica la posizione del frammento nel datagramma corrente, espressa in blocchi di 8 byte (max. 8192 frammenti).
- **TTL (8 bit):** Numero max di salti; si decrementa ad ogni passaggio, quando arriva a 0 il pacchetto viene eliminato.
- **Protocol (8 bit):** Protocollo di livello superiore (ICMP=1,TCP=6, UDP=17, ..)
- **Header Checksum (16 bit):** Checksum dell’**header**
	- ricalcolato da ogni router , perché il TTL cambia ad ogni salto.
	- Aiuta a rilevare errori generati da locazioni di memoria difettose nei router.
	- Somma tutte le sequenze di 16 bit (con l’aritmetica del complemento a 1) e poi prende il complemento a 1 del risultato.
- **Source e Destination Address (32+32 bit):** Indirizzi di sorgente e destinazione
- **Options**: Pensato per poter aggiungere estensioni non previste, formato: Opt. code (1 byte) - Opt. Length (1byte) - Opt. Data (n Byte)
	- 0 - End of Option List
	- 130 - Security: lista di reti vietate, non usato.
	- 7 - Route record: ogni router aggiunge il proprio indirizzo
	- 68 - Time Stamp: ogni router aggiunge il proprio indirizzo e data/ora.
	- 137 - Source routing: lista dei router da percorrere
- **Padding:** bit aggiunti per rendere il campo Options multiplo di 32 bit

---
## Indirizzi IP
Un indirizzo IP è un identificatore numerico assegnato a ciascun dispositivo che fa parte di una rete, viene utilizzato per instradare i dati attraverso Internet o reti locali.
Indirizzi a 32 bit con notazione **dotted decimal**: 4 decimali (0-255 = (2^8)-1) separati da punto, numero massimo di indirizzi = 2^32.
Per motivi di routing la sequenza è suddivisa in due parti:
-  **NET-id**: Questa parte dell'indirizzo IP identifica una rete di livello 2. I router utilizzano questa informazione per instradare i pacchetti attraverso la rete globale.
- **HOST-id**: Questa parte distingue gli host all'interno della stessa rete. In altre parole, se due dispositivi si trovano sulla stessa rete, la parte HOST-id permette di identificarli univocamente all'interno di quella rete specifica.

Gli indirizzi IP vengono <mark style="background: #946EFA;">classificati</mark> a seconda delle dimensioni della rete. Tradizionalmente, esistono tre classi principali di indirizzi IP, con ulteriori sottoclassi e specializzazioni:

1. **Classe A**: Gli indirizzi di Classe A sono destinati alle grandi organizzazioni o provider di servizi Internet. La parte più significativa (i primi bit) di un indirizzo di Classe A è riservata per identificare la rete, mentre il resto è usato per gli host. Gli indirizzi di Classe A iniziano con un **valore compreso tra 0 e 127** nel primo ottetto.

2. **Classe B**: Gli indirizzi di Classe B sono utilizzati per organizzazioni di medie dimensioni. Hanno una porzione di rete più ampia rispetto alla Classe A. Gli indirizzi di Classe B iniziano con un **valore compreso tra 128 e 191** nel primo ottetto.

3. **Classe C**: Gli indirizzi di Classe C sono utilizzati per organizzazioni più piccole. Hanno una porzione di rete ancora più ampia rispetto a Classe B. Gli indirizzi di Classe C iniziano con un **valore compreso tra 192 e 223** nel primo ottetto.

4. **Classe D**: Gli indirizzi di Classe D sono riservati per l'uso multicast. Non vengono assegnati a singoli host o reti.

5. **Classe E**: Gli indirizzi di Classe E sono riservati per usi futuri o sperimentali. Non vengono utilizzati comunemente in reti Internet pubbliche.

Oggi, l'assegnazione degli indirizzi IP è spesso basata su [[#CIDR - Classless Inter-Domain Routing]], che permette una distribuzione più flessibile e efficiente degli indirizzi. Questo ha reso meno rilevante la classificazione tradizionale di Classe A, B e C. Inoltre, con l'adozione crescente di IPv6, che utilizza un formato completamente diverso e offre un numero praticamente illimitato di indirizzi, l'architettura di indirizzamento IP sta subendo un'evoluzione significativa.

| Classe | Bit-Iniziali | Inizio    | Fine      | Indirizzi | Default-Mask  | CIDR |
| ------ | ------------ | --------- | --------- | --------- | ------------- | ---- |
| A      | 0            | 0.x.x.x   | 127.x.x.x | 2G        | 255.0.0.0     | /8   |
| B      | 10           | 128.x.x.x | 191.x.x.x | 1G        | 255.255.0.0   | /16  |
| C      | 110          | 192.x.x.x | 223.x.x.x | 0.5G      | 255.255.255.0 | /24  |
| D      | 1110         | 224.x.x.x | 239.x.x.x | 0.25G     | Multicast     |      |
| E      | 1111         | 240.x.x.x | 255.x.x.x | 0.25G     | Reserved              |      |

Se la parte Host è di N bit, il numero di indirizzi effettivamente assegnabili agli host è **(2^N)-2**, poiché il primo indirizzo (tutti zeri nella parte host) identifica la rete, mentre l'ultimo indirizzo (tutti uni nella parte host) è l'indirizzo di broadcast

**LOOPBACK**: IP per uso privato
La rete 127.0.0.0/16 è riservato per il loopback (RFC 3330).
Per convenzione su ogni host viene definita una interfaccia virtuale di loopback con indirizzo IP predefinito 127.0.0.1, con nome **localhost**, che consente la comunicazione TCP/IP tra due processi locali senza il coinvolgimento di interfacce fisiche.

### Subnetting
Questa suddivisione delle classi ha portato a uno spreco di indirizzi IP, specialmente nelle reti più piccole. Per affrontare questo problema, è stato sviluppato il subnetting.
Il subnetting è una tecnica utilizzata nelle reti informatiche per suddividere una rete IP più grande in sotto-reti più piccole. Questo consente di ottimizzare l'uso degli indirizzi IP e di gestire in modo più efficiente il traffico di rete.
A questo punto l'indirizzo IP viene suddiviso in:
1. **Parte di Rete**: Questa parte identifica la rete stessa. È composta da un insieme di bit fissi che definiscono la rete. Tutti i dispositivi all'interno della stessa rete condividono lo stesso prefisso di rete.
    
2. **Parte di Subnet**: Questa parte è utilizzata per suddividere ulteriormente la rete in sotto-reti più piccole. I dispositivi all'interno della stessa sotto-rete condividono il prefisso di rete e il prefisso di subnet.
    
3. **Parte di Host**: Questa parte identifica un dispositivo specifico all'interno della rete o della sotto-rete. Ogni dispositivo all'interno della rete o della sotto-rete avrà un indirizzo univoco all'interno di questa parte.

**Come funziona il subnetting?**
Ho bisogno di una maschera di sottorete (Subnet Mask), è un valore numerico che mi indica quanti bit dedico alla parte di rete e quanti alla parte di host.
Supponiamo di avere una maschera di sottorete di 255.255.255.0 (comunemente scritta come /24).
Il "/24" indica che i primi 24 bit dell'indirizzo IP (**8bit**.**8bit**.**8bit**.8bit) sono riservati per la parte di rete. Questa rappresentazione è molto utile perché fornisce un modo semplice ed efficiente per comunicare la dimensione della rete.
Quando si tratta di subnetting, i bit riservati alla parte di rete definiscono quanti indirizzi IP sono disponibili all'interno di quella subnet. In questo caso, con una maschera di sottorete "/24", avrai 24 bit per la rete e 8 bit per gli host, che significa 2^8 = 256 indirizzi IP disponibili all'interno di quella subnet.
#### CIDR - Classless Inter-Domain Routing
Soluzione temporanea in attesa di IPv6, assegna gli indirizzi IPv4 rimanenti in blocchi di dimensione variabile nella forma Indirizzo/Mask es. 160.87.64.0/15.

--- 
<span style="color: #946EFA;"> Esercizio: </span>

Supponiamo di avere un blocco di indirizzi IP di Classe C: 192.168.1.0/24. Questo significa che abbiamo 256 indirizzi IP disponibili (da 192.168.1.0 a 192.168.1.255).

Avendo una maschera di sottorete pari a 255.255.255.0 (i primi 24 bit occupati per la rete quindi pongo i bit = 255, gli ultimi 8 bit dedicati agli host quindi pongo il bit a 0),  se volessi suddividere ulteriormente la mia rete in 4 sotto-reti come faccio?

Sicuramente abbiamo bisogno di 2 bit per la rappresentazione delle 4 sotto-reti (2^nBit = 4 -> 2^**2** = 4), quindi dedichiamo 2 bit alla parte subnet e rimangono 6 bit per la parte di host (poiché abbiamo utilizzato 2 bit per la subnet su un totale di 8 bit disponibili in un indirizzo IPv4).
Ricalcoliamo la subnet mask, dato che abbiamo riservato 2 bit per la parte di subnet, la nuova maschera di sottorete sarà /26 (poiché ci sono 26 bit riservati per la parte di rete e di subnet).
Come la scriviamo? 255.255.255.192, come ci arrivo? Essendo che i primi 26 bit sono occupati dalla parte di rete dovrò porre i bit = 1, quindi avrò un indirizzo del tipo: 11111111.11111111.11111111.11000000, in questo modo ho occupato 26 bit per l'indirizzo di rete (26 bit = 1), ora convertiamo i bit in decimali -> 11111111 = 2555; 11000000 = 192; -> 255.255.255.192.

---
<span style="color: #946EFA;"> Esercizio: </span>

*La classe C 192.1.1.0 viene assegnata a 3 Dipartimenti A (100 host) , B (60 host) e C (40 host), ciascuno con la propria LAN. 
Determinare il subnetting ottimale per questa situazione.*

Dobbiamo considerare il numero di host richiesti per ciascun dipartimento e decidere quante sotto-reti creare.
Inoltre, dobbiamo tenere conto del fatto che la rete di classe C 192.1.1.0 ha di base 256 indirizzi IP disponibili (/24, quindi mi rimangono solo 8 bit per gli host = 256).

**Dipartimento A**: Richiede 100 host, dato che il numero di host richiesti è superiore a 64 (2^6), avremo bisogno di almeno 7 bit per gli host (2^7 = 128 host). Quindi, riserveremo 7 bit per la parte di host.
**Dipartimento B**: Richiede 60 host. Con 6 bit per gli host (2^6 = 64 host), soddisfiamo il requisito. Quindi, riserveremo 6 bit per la parte di host.
**Dipartimento C**: Richiede 40 host. Anche qui, 6 bit per gli host sono sufficienti, quindi riserveremo 6 bit per la parte di host.

Quindi possiamo dedurre che il subnetting ottimale sia:

**Dipartimento A:** 7 bit per gli host, nTotBit - nBitHost = 32 - 7 = 25 arriviamo ad avere 192.1.1.0/25

**Dipartimento B:** 6 bit per gli host, 32 - 6 = 26, arriviamo ad avere 192.1.1.0+128 = 192.1.1.126/26

**Dipartimento C:** 6 bit per gli host, 32 - 6 = 26, arriviamo ad avere 192.1.1.128+64 = 192.1.1.192/26

---

### Supernetting
Il supernetting, noto anche come aggregazione di reti, è il processo opposto al subnetting. Invece di suddividere una rete in sotto-reti più piccole, il supernetting combina reti più piccole in una rete più grande. Questo viene fatto per semplificare le tabelle di routing e ridurre il carico sui router.

Esempio:
Un'azienda di contabilità ha 150 filiali per ciascuno dei 50 distretti geografici dove opera. In ogni filiale è presente un router connesso tramite [Frame Relay](https://it.wikipedia.org/wiki/Frame_Relay "Frame Relay") al quartier generale dell'azienda. Senza il supernetting, la tabella di routing di ciascuno di questi router dovrebbe tenere traccia di 150 router per ciascuno dei 50 distretti, per un totale di 7500 reti. Se però venisse implementato un sistema di indirizzamento gerarchico con il supernetting, collegando ciascuna filiale a un punto di interconnessione centralizzato che raggruppa tutte quelle dello stesso distretto, si potrebbero aggregare le rotte prima che vengano annunciate agli altri distretti. In questo modo, ciascun router sarà a conoscenza della propria subnet e di appena 49 rotte aggregate.

La determinazione delle rotte aggregate da parte di un router implica il riconoscimento del numero di bit di ordine più alto che sono comuni a tutti gli indirizzi. Per esempio, un router che possiede le seguenti reti nella sua tabella di routing calcola la rotta aggregata come di seguito:

```
 192.168.98.0
 192.168.99.0
 192.168.100.0
 192.168.101.0
 192.168.102.0
 192.168.105.0
```

Per prima cosa gli indirizzi vengono convertiti in formato binario e allineati in una lista:

![[supernetting1.png]]

In secondo luogo, vengono identificati i bit comuni, mostrati in rosso. Infine, viene contato il numero di bit comuni. La rotta aggregata viene calcolata impostando a zero i bit rimanenti, come mostrato sotto. Viene seguita da uno slash e dal numero di bit comuni.

![[supernetting2.png]]

La rotta aggregata è 192.168.96.0/20. La subnet mask è 255.255.240.0. Questa rotta contiene anche reti che non erano presenti nel gruppo iniziale, vale a dire 

```
192.168.96.0
192.168.97.0
192.168.103.0
192.168.104.0
192.168.106.0
192.168.107.0
192.168.108.0
192.168.109.0
192.168.110.0
192.168.111.0
```

Bisogna avere la certezza che queste reti non esistano nelle direzioni opposte a questa rotta. 
In un altro esempio, a un ISP viene assegnato, da parte di un RIR, un blocco di indirizzi IP che va da 172.1.0.0 a 172.1.255.255. L'ISP può assegnare questi indirizzi ai propri clienti nel seguente modo, al cliente A verrà assegnato il range da 172.1.1.0 a 172.1.1.255, al cliente B il range da 172.1.2.0 a 172.1.2.255, al cliente C il range da 172.1.3.0 a 172.1.3.255 e così via. Invece di avere singole voci per le subnet 172.1.1.x, 172.1.2.x, 172.1.3.x et cetera, l'ISP può aggregare l'intero range di indirizzi 172.1.x.x e annunciare la rete 172.1.0.0/16, allo scopo di ridurre il numero di voci globali nella tabella di routing.

---

## Instradamento dei datagrammi
La rete a cui appartiene un host è cruciale per decidere come inviare i dati a destinazione. Questa comunicazione può avvenire in due modi: direttamente o attraverso un percorso intermediario (indiretta).
- **Direct Delivery**: host sorgente e host destinatario condividono la stessa rete, trova l'indirizzo fisico del destinatario con l'ARP (Address Resolution Protocol - permette di trovare l'indirizzo MAC di un dispositivo all'interno di una rete locale quando si conosce il suo indirizzo IP) e lo associa all'IP del destinatario. Infine inoltra il pacchetto al livello link indirizzando il destinatario.
	Come funziona?
	- **Richiesta ARP (ARP Request)**: Quando un dispositivo nella rete ha bisogno di comunicare con un altro dispositivo nella stessa rete locale, ma non conosce l'indirizzo MAC del destinatario, invia una richiesta ARP broadcast. Questa richiesta contiene l'indirizzo IP del destinatario e chiede a tutti i dispositivi nella rete locale di rispondere con il loro indirizzo MAC se corrisponde all'indirizzo IP cercato.
	- **Risposta ARP (ARP Reply)**: Se si trova il dispositivo con l'indirizzo IP corrispondente risponde con il proprio indirizzo MAC tramite una risposta ARP, questa risposta viene inviata direttamente al dispositivo che ha iniziato la richiesta ARP, altrimenti se non si trova il pacchetto viene instradato al default gateway (router di default).
	- **Aggiornamento della Tabella ARP (ARP Cache)**: Il dispositivo che ha richiesto l'indirizzo MAC mantiene una tabella ARP che memorizza temporaneamente le corrispondenze tra gli indirizzi IP e MAC dei dispositivi nella rete locale. In questo modo, non è necessario effettuare richieste ARP per ogni pacchetto inviato.
- **Indirect Delivery**: sorgente e destinatario appartengono a reti IP diverse, individua il router da contattare consultando la propria **Tabella di routing**, trova l'indirizzo MAC del router tramite ARP che associa all'IP del destinatario, infine inoltra il pacchetto al livello Link indirizzando il router.

---

## Tabella di Routing
Essa contiene informazioni utilizzate dai dispositivi di rete per determinare la strada ottimale attraverso la quale inviare i pacchetti dati verso le destinazioni desiderate.
Ecco cosa trovi solitamente in una tabella di routing:
1. **Indirizzo di Destinazione**: Si tratta dell'indirizzo IP del destinatario a cui si intende inviare i dati.
2. **Gateway di Default o Router**: Specifica l'indirizzo del router o del dispositivo di rete al quale inviare i dati se la destinazione non si trova nella rete locale.
3. **Maschera di Sottorete**: Indica quale parte dell'indirizzo IP identifica la rete e quale parte identifica l'host.
4. **Interfaccia di Uscita**: Indica l'interfaccia di rete (ad esempio, ethernet, Wi-Fi) che deve essere utilizzata per inoltrare il pacchetto verso la destinazione.

---

## NAT - Network Address Translation
Dispositivo che consente agli host di una LAN (con indirizzi privati) di comunicare in Internet utilizzando un solo indirizzo pubblico.
La linea verso Internet possiede un indirizzo IP pubblico e viene visto dagli host della LAN come Default Router.
Le operazioni del NAT sono distinte in base alla direzione:
- **SNAT (Source-NAT)** è la funzionalità che consente di manipolare l'indirizzo sorgente ed è tipicamente utilizzato per consentire ai pacchetti di una LAN privata di uscire in internet. 
  Quando un Host della LAN si rivolge al NAT per uscire in Internet il NAT trasforma l’indirizzo del mittente IP nell'indirizzo IP pubblico del NAT, quindi contatta il destinatario.
- **DNAT (Destination-NAT)** è utilizzata per manipolare l'indirizzo di destinazione.
  E' usata tipicamente per dirottare verso una destinazione interna (con indirizzo privato) i pacchetti provenienti da Internet.

Le manipolazioni SNAT e DNAT sono rappresentate in tabelle che vengono consultate per ogni pacchetto che attraversa il NAT. Le informazioni memorizzate nelle tabelle (entry) possono essere statiche o dinamiche.
1. **Entry Statiche**: Se vogliamo avere un server interno che deve essere contattato da un client esterno dobbiamo istruire il NAT mediante una entry statica che associa una porta del NAT con IP/porta del server interno.
    Quando un client esterno contatta il NAT sulla porta viene consultata la entry statica e applicato **DNAT**. 
    Viene inoltre creata una entry dinamica che verrà utilizzata per applicare SNAT sulla risposta.
2. **Entry Dinamiche**: Quando un client della LAN si rivolge al NAT per contattare un server esterno, il NAT genera una entry dinamica associando IP/porta del client con la IP/porta del server quindi applica **SNAT**.
    L'entry viene utilizzata per il DNAT sulla risposta del server.

**Problematiche**
- Violazione dell'univocità degli indirizzi: migliaia di Host usano gli stessi indirizzi privati.
- Sicurezza: è difficile tracciare l’identità dell’indirizzo IP pubblico.
- IP non è più connection-less
- IP non è più stratificato: Il Layer IP non dovrebbe entrare nei layer superiori
- Un guasto al NAT pregiudica tutte le connessioni che lo attraversano.

>In realtà NAT ha avuto una grande diffusione e ha ridotto la spinta verso IPv6.

---

## ARP - Address Resolution Protocol
Ogni interfaccia di rete di un nodo (Ethernet, LAN Wireless, Seriale, ecc) possiede un indirizzo MAC (o fisico) e, se utilizzata in internet, almeno un indirizzo IP.
Il protocollo **ARP (Address Resolution Protocol)** ha il compito di determinare l’indirizzo fisico di un nodo IP.
Quando un nodo mittente deve contattare un destinatario in **Direct Delivery** (Terminale o Router) di cui conosce solo l’indirizzo IP utilizzerà il protocollo ARP.
Il frame ARP contiene:
- Un campo codice 1 = ARPrequest, 2 = ARPreplay.
- indirizzo IP e Indirizzo HW di partenza e destinazione.

---

## RARP - Reverse ARP
In determinate situazioni alcuni nodi IP al momento dell’attivazione della rete non conoscono il loro indirizzo IP (ad esempio perché non hanno memoria permanente).
Esistono diverse soluzioni, tra cui **RARP** (Reverse ARP).
E' un protocollo ideato da SUN per risolvere il problema.
Il client invia in modalità Broadcast la richiesta:
- “Questo è il mio indirizzo MAC: xx-xx-xx-xx-xx-xx, Qualcuno conosce il mio indirizzo IP?”.
Un server RARP, con la tabella MAC-IP , risponderà con l’informazione richiesta.
Svantaggi:
- la richiesta Broadcast non passa i router
- le associazioni MAC-IP sono statiche
- non sono previste altre informazioni
RARP è reso obsoleto dal suo successore DHCP.

---

## DHCP - Dynamic Host Configuration Protocol
è un protocollo di rete utilizzato per assegnare automaticamente indirizzi IP e altre informazioni di configurazione di rete a dispositivi all'interno di una rete locale.
Funzionamento:
1. **Richiesta di Configurazione**: Quando un dispositivo si collega a una rete che utilizza il DHCP, invia un messaggio di richiesta per ottenere un indirizzo IP e altre informazioni di rete.
2. **Risposta del Server DHCP**: Un server DHCP all'interno della rete riceve la richiesta e seleziona un indirizzo IP disponibile dal suo pool. Questo indirizzo viene quindi assegnato al dispositivo.
3. **Configurazione Aggiuntiva**: Oltre all'indirizzo IP, il server DHCP può fornire al dispositivo altre informazioni di configurazione, come la maschera di sottorete, il gateway predefinito, i server DNS, ecc.
4. **Utilizzo dell'Indirizzo Assegnato**: Il dispositivo utilizza l'indirizzo IP e le altre informazioni di configurazione ricevute per configurare la sua connessione di rete e comunicare all'interno della rete.
5. **Periodo di Affitto (Lease)**: L'indirizzo IP assegnato ha un periodo di "affitto", ovvero una durata specificata dal server DHCP. Durante questo periodo, il dispositivo può utilizzare l'indirizzo senza dover richiedere una nuova configurazione.
6. **Rinnovo dell'Affitto**: A metà del periodo di affitto, il dispositivo può richiedere al server DHCP di rinnovare l'affitto dell'indirizzo IP. Se il server accetta, il periodo di affitto viene esteso.

---

## ICMP - Intenet Control Message Protocol
è un protocollo di servizio di IP per lo scambio di messaggi di errore o di controllo che consentono agli Host e ai Router di accorgersi di eventuali malfunzionamenti della rete.
Spedisce i messaggi di notifica dell'errore sempre al mittente del datagramma per il quale si è verificato l'errore.
l formato del frame è costituito da una intestazione e da un'area dati. 
La prima è composta da tre campi:
- **TIPO** è un numero di 8 bit che identifica il messaggio.
- **CODICE:** Info aggiuntive. Ad esempio se il Tipo è 3 il Codice dice qual'è il tipo di errore.
- **CHECKSUM**, di 16 bit, è il CRC del frame ICMP (header+data).