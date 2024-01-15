```table-of-contents
```
---

# TFTP vs FTP
TFTP (Trivial File Transfer Protocol) è la versione semplificata di FTP (File Transfer Protocol), che è stato sviluppato per il trasferimento efficiente ed affidabile dei dati, infatti si basa su TCP.
Il server FTP offre anche un servizio di autenticazione per l'accesso al file-system, la gestione delle directory (navigazione, creazione, cancellazione) e dei file.

Altra caratteristica peculiare è quella di usare due porte: la TCP/21 (comandi) e la TCP/20 (dati).

Le modalità di funzionamento sono due: attiva e passiva.
- Nella *modalità attiva* il client apre il canale comandi verso il server (porta 21 del server), mentre per la trasmissione dati il client svolge la funzione di server, ovvero rimane in ascolto sulla porta > 1024 mentre il server si comporta da client utilizzando la porta 20. In genere le politiche di sicurezza impediscono l’accesso alle porte dei client bloccando questa modalità. 
- Nella modalità passiva* il server indica al client la porta > 1024 da utilizzare per il trasferimento dei dati.

TFTP non supporta l'autenticazione e utilizza UDP, con il server in ascolto sulla porta 69. Questo significa che la gestione del flusso (numerazione dei pacchetti, Acknowledgement, gestione degli errori) viene realizzata a livello applicativo, all'interno di TFTP.

---

## TFTP
Ogni trasferimento inizia con una richiesta di read `GET` o write `PUT`. 
Con la chiamata `GET` il server risponde con un file che viene frammentato in datagrammi numerati; ogni datagramma deve essere riscontrato (ACK).

La grandezza del blocco dedicato ai dati di default è di 512 byte. Quindi un pacchetto con una dimensione di dati inferiore a 512 byte rappresenterà l'ultimo pacchetto trasmesso.

### Esempio di trasmissione
Opcode (16 bit) identificano il tipo di pacchetto:
1. RRQ: Read Request
2. WRQ: Write Reques
3. DATA
4. ACK
5. ERROR

Vediamo la trasmissione dei frammenti in una comunicazione tra Client e Server:
1. **CLIENT**: Read/Write Request Packet (`GET` / `PUT`), pacchetto spedito all'inizio della conversazione:

![[RRQ_WRQ_Packet.png]]

2. **SERVER**: Data packet, manda i dati divisi in frammenti di massimo 512 Byte:

![[DataPacket.png]]

3. **CLIENT**: ACK Packet, una volta ricevuto il primo pacchetto di dati risponde con un ACK Packet:

![[ACKPacket.png]]

Esiste anche un pacchetto di errore, ERROR Packet, che viene inviato in caso si riscontri un errore durante la trasmissione dei dati (al posto dell'ACK):

![[ErrorPacket.png]]

I pacchetti vengono quindi inviati finché la loro dimensione non è inferiore a 512 Byte, dopo l'ultimo pacchetto termina la connessione.

![[SessioneTFTP.png]]

Comandi bash:
```bash
tftp -v <nome server> -c put /etc/hosts hosts
tftp -v <nome server> -c get hosts
```

---

# DNS
Il Domain Name System (DNS) è la "guida telefonica" di Internet. Le persone accedono alle informazioni online tramite dei nomi di dominio, come ad esempio `google.com`. I browser Web interagiscono tramite indirizzi Internet Protocol (IP). 
*Il DNS traduce i nomi di dominio in indirizzi IP, in modo che i browser possano caricare le risorse Internet.*

Lo spazio dei nomi è strutturato in modo gerarchico, come il file-system, ma la radice è a destra: il primo elemento è il nome locale del nodo, mentre gli elementi successivi (domini) rappresentano il percorso nella gerarchia e sono separati dal punto (`.`).

Esempio: 
```
didattica-linux.unipr.it
```

Il dominio più a destra (`it` nell’esempio) è detto Top Level Domain (TLD). 
Sono gestiti dall'organismo internazionale ICANN (attraverso la sua emanazione IANA) che li assegna alle organizzazioni che ne fanno richiesta, mentre i livelli successivi sono gestiti in modo autonomo dalle organizzazioni assegnatarie.

Sono 4 i server DNS coinvolti nel caricamento di una pagina web:
 1. Resolver ricorsivi
 2. Root nameserver
 3. TLD nameserver (top-level domain)
 4. Nameserver autoritativi
 
 Questi quattro server DNS lavorano insieme in armonia per completare l'attività di apparizione dell'indirizzo IP per un dominio specificato al client.

---

## DNS Client
Il primo server DNS coinvolto nel caricamento di una pagina web e' il DNS client.
Un DNS client contiene un componente software, detto *Resolver*, che ha il compito di risolvere la richiesta.

Dopo aver ricevuto una query DNS da un client Web, un resolver ricorsivo risponderà con i dati memorizzati nella cache o invierà una richiesta a un root nameserver vicino, seguita da un'altra richiesta a un TLD nameserver e quindi un'ultima richiesta a un nameserver autoritativo. 

Dopo aver ricevuto una risposta dal nameserver autoritativo contenente l'indirizzo IP richiesto, il resolver ricorsivo invia quindi una risposta al client.

Durante questo processo, il resolver ricorsivo memorizzerà nella cache le informazioni ricevute dai nameserver autoritativi.

![[DNS_Server.png]]

Nei sistemi Linux questa configurazione viene stabilita nel file `/etc/resolv.conf`. 

> *Esempio*: `name-server 160.78.48.10`, significa che il dispositivo utilizzerà il server DNS con indirizzo IP `160.78.48.10` per risolvere i nomi del dominio.

La configurazione del *DNS* può essere impostata staticamente oppure **dinamicamente** dal protocollo DHCP. 
Quando un dispositivo si connette a una rete, il protocollo DHCP può assegnare dinamicamente un indirizzo IP, un gateway, una netmask e anche uno o più server DNS al dispositivo.

Vista la criticità del servizio DNS, un client dichiara tipicamente almeno 2 DNS Forwarder per ridondanza.

Un **DNS forwarder** è un server DNS a cui il server DNS client si rivolge per ottenere risposte alle richieste di risoluzione dei nomi di dominio che non sono presenti nella sua cache locale. 

La ridondanza è importante per assicurare che se un server DNS fallisce, l'altro possa ancora gestire le richieste di risoluzione dei nomi di dominio.

In un programma applicativo il ruolo di Resolver è svolto dalla funzione `gethostbyname()`.

---

## Root Server
Il secondo server DNS coinvolto nel caricamento di una pagina web e' il Root Server.

Internet possiede 13 Root Server che contengono le informazioni riguardo i domini di primo livello. Questi server vengono contattati ogni volta che un client chiede informazioni relative ad altri TLD, quindi ogni DNS Forwarder deve possedere una lista aggiornata dei Root Server (file named.ca di Bind).
I Root NS sono iterativi: se non hanno la risposta forniscono l'indirizzo del server del
TLD coinvolto.

![[RootServer.png]]

---

## TLD
Il terzo server DNS coinvolto nel caricamento di una pagina web e' il TLD nameserver.

Un TLD nameserver (Top Level Domain) conserva le informazioni per tutti i nomi di dominio che condividono un'estensione di dominio comune, come `.com`, `.net` o qualunque cosa venga dopo l'ultimo punto in un URL.

Ad esempio, un TLD nameserver `.com` contiene informazioni per ogni sito Web che termina in `.com`. Se un utente cercasse `google.com`, dopo aver ricevuto una risposta da un root nameserver, il resolver ricorsivo avrebbe quindi inviato una query a un TLD nameserver `.com`, che avrebbe risposto indicando il nameserver autoritativo per quel dominio.

Inizialmente Internet era composta unicamente da nodi americani, per cui esistono alcuni TLD che rispecchiano la strutturazione Statunitense originale (1985): 
- `com` (commerciali), `edu` (istituzioni educative), `gov` (governo federale US), `mil` (forze armate US), `net` (provider di rete), `org` (organizzazioni no-profit).

Successivamente, con la diffusione di Internet, sono nati i TLD geografici nazionali: 
- *it*, *es*, *fr*, *de*, *gr*, *ca*, *at*, *au*, *be*, *nl*, *pt*, *ch*, ...

A partire dal 2000 ICANN ha approvato diversi nuovi nomi TLD generici quali: 
- *biz* (business), *info* (informazioni), *name* (nome di persona), *pro* (professionisti), *coop* (cooperative), *museum* (musei), *travel* (viaggi), *aero* (aerotrasporti).

![[TLD.png]]

### Zone del DNS
Le zone nel contesto sono rappresentate dai domini di primo livello (TLD) e dai loro sottodomini. I domini di primo livello come .com, .edu, .it, .org e così via, costituiscono ciascuno una zona distinta nel sistema DNS e possono creare sottodomini di livello 2, i quali a loro volta possono gestire domini di livello 3 e cosi via.

> Esempio: Il dominio di primo livello `.it` rappresenta una zona, e il suo spazio dei nomi include tutti i sottodomini sotto `.it`, come ad esempio `unipr.it`.

Per ogni Zona il server DNS primario è responsabile dell'autorità sulla zona. Gestisce e mantiene le informazioni sulla zona, come gli indirizzi IP associati ai nomi di dominio all'interno della zona ed è anche responsabile della ricezione delle modifiche e delle aggiunte alle informazioni della zona.

I server DNS secondari sono server di backup che replicano i dati dalla zona del server DNS primario, il che significa che mantengono una copia aggiornata dei dati dalla zona del server primario. Questa replicazione offre sia sicurezza (nel caso in cui il server primario diventi inaccessibile) che prestazioni (distribuendo il carico di query DNS).

#### Processo di delega
Il **processo di delega** coinvolge principalmente due zone: la zona superiore (il "padre") e la zona inferiore (la "figlia"). La zona superiore può decidere di delegare l'autorità su una porzione specifica del suo spazio dei nomi alla zona inferiore. Questo avviene attraverso l'uso del record NS (Name Server).
Quando una zona è delegata, la zona superiore aggiunge uno o più **record NS** per indicare i server DNS responsabili per la zona inferiore, questi record NS contengono il nome del server DNS e il relativo indirizzo IP.

Il processo di delega attraverso record NS consente di distribuire la gestione dei nomi di dominio in modo gerarchico, migliorando l'efficienza e la scalabilità del sistema DNS.
Ogni nuovo host viene inserito tipicamente sia nella zona per la risoluzione diretta che nella zona per la risoluzione inversa.

![[zone_DNS.png]]

---

## DNS Server autoritativo
L'ultimo server DNS coinvolto nel caricamento di una pagina web e' il DNS Server autoritativo.

Quando un resolver ricorsivo riceve una risposta da un TLD nameserver, tale risposta indirizzerà il resolver a un nameserver autoritativo. Il nameserver autoritativo è di solito l'ultimo passo del resolver nel viaggio verso un indirizzo IP. 

Il nameserver autoritativo contiene informazioni specifiche sul nome di dominio che serve. 
Può fornire ad un resolver ricorsivo l'indirizzo IP di quel server trovato nel record DNS (Address).
Se il dominio ha un record CNAME (alias) fornirà al resolver ricorsivo un dominio alias: a quel punto il resolver ricorsivo dovrà eseguire una ricerca DNS completamente nuova per ottenere un record da un nameserver autoritativo (spesso un record A contenente un indirizzo IP).

Un server può essere configurato per diversi tipi di funzionamento:
- **Server autoritativo di zona Primario o Secondario**
	- L'amministratore di Zona aggiorna i dati sul Primario. 
	- I server Secondari si sincronizzano con il primario replicando tutta la Zona (“Zone Transfer”) attraverso un Data-Pull sulla porta 53/TCP. 
	- Risponde alle query che riceve (53/UDP). 
	- Un server Autoritativo è generalmente anche Forwader NS.
- **Server Forwarder (o Caching Name Server)**: 
	- Riceve query dai client (53/UDP) 
	- Ottiene la risposta interrogando i Server Autoritativi 
	- Mantiene copia locale in Cache delle risposte ottenute 
	- Invia la risposta al client

---

### Risoluzione Ricorsione e Iterativa
Se il server che riceve la richiesta è autoritativo per il dato richiesto risponde direttamente, altrimenti occorre attraversare l'albero passando attraverso i server autoritativi coinvolti. L'attraversamento può essere **ricorsivo o iterativo**: 
- Modalità Ricorsiva: se il server interrogato non è autoritativo per il dato richiesto, passa la richiesta al server successivo e cosi via in modo ricorsivo. 
- Modalità Iterativa: il server restituisce al client l'indirizzo del server successivo. In questo modo è il DNS locale che contatta direttamente i server coinvolti.

Generalmente, un server ammette query ricorsive solo per i client locali.

Ricorsivo:
![[query.png]]

Iterativo:
![[processo_iterativo.png]]

### Risoluzione inversa
La **risoluzione inversa** consiste nella risoluzione del nome a partire dall'indirizzo IP. Viene usata ad esempio per produrre un output leggibile nei file di log, oppure per controlli di autenticazione (e.g. richiedere che il client sia registrato).
Il nome dei domini di Reverse è composto dai numeri della rete (in ordine rovesciato), seguiti dalla stringa “in-addr.arpa” (TLD per la risoluzione inversa). Il rovesciamento del numero consente di ricercare i numeri nello stesso albero dei nomi, utilizzando lo stesso procedimento di parsing da destra verso sinistra.

> *Esempio*: `10.48.78.16.in-addr.arpa` è il nome di `caio.cce.unipr.it` nel ramo della risoluzione inversa.

Comandi bash:
```bash
dig PTR 10.48.78.160.in-addr.arpa
dig -x 160.78.48.10
dig -x 160.78.48.10 +trace
# -x -> semplifica il reverse search
# +trace -> dig esegue query iterative (non delega il forwarder)
```

![[reverse_resolution.png]]

---

### Resource Record
Le informazioni relative alla zona vengono memorizzate come Resource Record (RR).
Il formato generico di un RR dispone dei seguenti campi: 
- Nome: Il nome di dominio a cui questo RR si riferisce. 
- TTL: Tempo di vita del RR nella cache dei server DNS prima di essere scartato.
- Classe: Identifica la famiglia di protocollo, IN che indica il sistema Internet. 
- Tipo: Il tipo di RR, i tipi principali sono: 
	- A: Il più usato, indica l'indirizzo IPv4 per il nome specificato. 
	- AAAA: Indica l'indirizzo IPv6 (eventuale) associato al nome. 
	- CNAME: Record Canonical Name, usato per indicare un nome di alias. 
	- MX: Mail eXchanger, indica un host che gestisce la posta per il dominio. 
	- NS: Un server DNS per il dominio specificato. 
	- PTR: Usato nella risoluzione inversa per associare un indirizzo IP al nome. 
	- SOA: Start of Authority, un RR che indica il server DNS dove risiedono i dati autoritativi per questo dominio ed alcuni dati amministrativi.

Esempio:

```bash
> dig google.com                                                                                   

; <<>> DiG 9.10.6 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57156
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		68	IN	A	216.58.205.46

;; Query time: 9 msec
;; SERVER: fe80::1%10#53(fe80::1%10)
;; WHEN: Mon Jan 15 09:09:03 CET 2024
;; MSG SIZE  rcvd: 55
```

---

## Posta Elettronica
Per ogni dominio che è in grado di ricevere posta, il DNS è in grado di fornire una lista di server SMTP (Simple Mail Transfer Protocol) a cui inviare il messaggio. In questo modo, se il mail server principale del destinatario non è operativo, è possibile inviare il messaggio verso un computer di backup in grado di gestire la posta altrettanto bene. 
Queste informazioni sono contenute nei record MX (Mail eXchanger).

Esempio:
```bash
> dig google.com MX                                                                                  

; <<>> DiG 9.10.6 <<>> google.com MX
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53673
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 10

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;google.com.			IN	MX

;; ANSWER SECTION:
google.com.		269	IN	MX	10 smtp.google.com.

;; ADDITIONAL SECTION:
smtp.google.com.	264	IN	A	108.177.127.26
smtp.google.com.	264	IN	A	142.251.31.26
smtp.google.com.	264	IN	A	142.251.31.27
smtp.google.com.	264	IN	A	172.217.218.26
smtp.google.com.	264	IN	A	172.217.218.27
smtp.google.com.	19	IN	AAAA	2a00:1450:4013:c07::1b
smtp.google.com.	19	IN	AAAA	2a00:1450:4013:c08::1a
smtp.google.com.	19	IN	AAAA	2a00:1450:4013:c08::1b
smtp.google.com.	19	IN	AAAA	2a00:1450:4013:c1a::1a

;; Query time: 9 msec
;; SERVER: fe80::1%10#53(fe80::1%10)
;; WHEN: Mon Jan 15 09:40:24 CET 2024
;; MSG SIZE  rcvd: 252
```

---

## Formato del pacchetto DNS
Tutti i pacchetti DNS hanno lo stesso formato di figura, composto da: 
- **Transaction ID**: serve per associare domanda a risposta 
- **16 Flags tra cui**: 
	- QR (domanda (0) / risposta (1)) 
	- OPCODE (4 bits, tipo di query) 
	- RD (Recursion Desired)
	- RA (Recursion Available) 
	- RCODE (4 bits, esito della risposta) 
- **4 sezioni**: 
	- QUESTIONS: domande per il DNS. 
	- ANSWERS: elenco di RR che rispondono alla Question.
	- AUTHORITY: elenco di RR degli NS autoritativi che portano più vicino alla risposta. 
	- ADDITIONAL: elenco di RR con informazioni addizionali.

![[dns_packet.svg]]

---

## DNSSEC - DNS Security Extensions
I Domain Name System Security Extensions (DNSSEC) sono una serie di specifiche dell'IETF (Internet Engineering Task Force) per garantire la sicurezza e affidabilità delle informazioni fornite dai sistemi DNS. 

Servizi offerti: 
- Autenticazione: garanzia sull’origine dei dati DNS.
- Integrità dei dati ricevuti (non la riservatezza).

Funzionamento: 
Ogni server DNSSEC possiede una coppia di chiavi crittografiche, una pubblica e una privata. 
La chiave privata viene utilizzata per firmare ogni Resource Record (RRset) generando un nuovo Record type, il RRsig. 
Il server pubblica anche la chiave pubblica introducendo il nuovo record type DNSkey. 
Il client, utilizzando la chiave pubblica del server può verificare l'autenticità della firma RRsig.

![[DNSSEC.png]]

---

## dDNS - DNS Dinamico
Il DNS Dinamico è una tecnologia che permette ad un nome DNS in Internet di essere sempre associato all'indirizzo IP di uno stesso host, anche se l'indirizzo cambia nel tempo (tipicamente computer portatili). 

Il servizio è costituito da una popolazione di client dinamici (host con indirizzo IP dinamico che vogliono che il loro IP attuale sia registrato nel DNS), da uno o più server DNS dinamici e da un protocollo di comunicazione tra le due parti. 

`nsupdate` è una utility disponibile ai client per l'aggiornamento del DNS. 
L'aggiornamento dinamico del DNS può essere fatto direttamente dal server dhcp.

![[dDNS.png]]

---

## IPv6
Gli indirizzi IPv6 sono rappresentati nel Domain Name System dal Record AAAA (detto anche record quadruplo-A) per il forward lookup (analogamente al Record A del IPv4); la risoluzione DNS inversa si appoggia sulla zona `ip6.arpa`. Questo schema di funzionamento viene descritto nel [RFC 3596](https://datatracker.ietf.org/doc/html/rfc3596).

![[dns_ipv6.png]]

Lo schema della quadrupla A è uno dei due proposti in fase di design del protocollo IPv6.

Sebbene lo schema AAAA sia una semplice generalizzazione dei DNS IPv4, lo schema A6 sarebbe stato un'estensione più generica, ma anche più complessa: 
- I record A6 avrebbero permesso ad un singolo indirizzo IPv6 di essere diviso in diverse sezioni gestite in zone differenti. Questo avrebbe permesso, ad esempio, di ridistribuire in maniera rapida la numerazione di un network.
- La delega degli indirizzi attraverso l'uso dei record NS sarebbe stata ampiamente sostituita dall'uso dei record DNAME (similmente agli attuali record CNAME, ma costituendo un intero albero di indirizzi). Questo avrebbe permesso la gestione unitaria dei lookup diretti ed inversi.
- Un nuovo tipo di dato chiamato bit label veniva introdotto nei nomi di dominio, principalmente per scopi di lookup inverso.

Lo schema AAAA è stato standardizzato nell'agosto del 2002 nel RFC 3363 (nel RFC 3364 sono valutati tutti i pro ed i contro di entrambi gli schemi proposti).

> Fonte: [Wikipedia](https://it.wikipedia.org/wiki/IPv6#IPv6_ed_i_Domain_Name_System).