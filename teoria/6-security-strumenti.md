```table-of-contents
```
# La sicurezza
Con il termine sicurezza informatica si intende quel ramo dell'informatica che si occupa dell'analisi delle vulnerabilità, del rischio, delle minacce e della successiva protezione dell'integrità logico-funzionale. 
La gran parte delle minacce derivano dalla rete Internet, per cui la sicurezza informatica è un tema importante nello studio delle reti di calcolatori.
La **politica di sicurezza** è quindi un compromesso, dettato dalle proprie necessità, tra il costo per attivarla ed il beneficio ottenuto in termini di diminuzione del rischio.

## Servizi di sicurezza
Per proteggere un host in rete o una comunicazione occorre stabilire dei servizi di sicurezza che possono essere classificati nel seguente modo:
- **Autenticazione** (Authentication): si tratta del processo mediante il quale l'identità di un utente, di un dispositivo o di un'applicazione viene verificata, questo implica tipicamente l'uso di credenziali come username e password, o metodi più avanzati come biometria, token hardware, certificati digitali, o autenticazione a due fattori (2FA) e multifattoriale (MFA).
- **Autorizzazione** (Authorization, Access Control): dopo che un utente o un dispositivo è stato autenticato e la sua identità è stata verificata, l'autorizzazione determina quali azioni o risorse specifiche possono essere accedute o eseguite da quella particolare entità.
- **Confidenzialità/Riservatezza** (Data Confidentiality): si riferisce alla protezione delle informazioni da accessi non autorizzati o divulgazioni non desiderate. L'obiettivo principale è assicurare che solo gli utenti autorizzati possano accedere a determinati dati e che questi dati siano mantenuti segreti e al sicuro.
- **Integrità dei dati** (Data Integrity): si concentra sulla garanzia che i dati non siano stati alterati in modo non autorizzato o accidentale durante il loro ciclo di vita. Garantire l'integrità dei dati è fondamentale per preservare la precisione, l'affidabilità e la coerenza delle informazioni.
- **Non ripudio** (Non-Repudiation): mira a fornire protezione contro il ripudio o la negazione delle azioni da parte degli utenti coinvolti in una comunicazione o transazione. Questo principio è spesso diviso in due aspetti principali:
	- Non ripudio della sorgente: una volta che un mittente ha inviato un messaggio o ha compiuto un'azione, non può negare in modo credibile di averlo fatto. Ciò è solitamente ottenuto attraverso l'uso di firme digitali o altri metodi di autenticazione avanzati che collegano in modo univoco un'azione o un messaggio a una specifica entità.
	- Non ripudio della destinazione: in questo contesto, una volta che la destinazione ha ricevuto i dati, non può negare in modo credibile di averli ricevuti. La conferma di consegna o altri meccanismi simili possono essere utilizzati per dimostrare che la destinazione ha effettivamente ricevuto e preso in carico i dati.
- **Disponibilità** (Avaliability): si concentra sulla protezione e assicurazione dell'accessibilità e dell'operatività di una risorsa di sistema o di rete. In altre parole, la disponibilità mira a garantire che le risorse siano sempre accessibili quando necessario e che il sistema sia in grado di erogare i servizi previsti senza interruzioni indesiderate.
- **Audit** (Accoutability, Traceability): coinvolge la registrazione e la monitorazione di eventi di sistema o di rete. L'obiettivo principale è fornire una traccia accurata delle attività che si verificano in un sistema, consentendo la ricostruzione degli eventi, l'individuazione di comportamenti sospetti e, in alcuni casi, la possibilità di addebitare responsabilità per determinate azioni.

## Metodi di attacco
- **Attacco passivo:** sono tattiche utilizzate dagli aggressori per raccogliere informazioni o intercettare comunicazioni senza alterare attivamente i dati o compromettere la disponibilità dei servizi. Questi attacchi sono spesso focalizzati sulla raccolta di informazioni sensibili o riservate.
	- **Raccolta di informazioni su possibili obiettivi**:
		- network monitor, port scanning, etc.
	- **Intercettazione delle comunicazioni (Confidentiality Attacks)**:
		- eavesdropping, Sniffing.
- **Attacco attivo:** rappresentano azioni da parte di un aggressore per manipolare o interrompere attivamente sistemi, reti o servizi.
	-  **Fabbricazione dell'identità di un'altra entità (Authentication attacks)**:
		- Spoofing, Man in the Middle
	- **Interruzione/compromissione di servizi (Avaliability attacks):**
		- Denial of Service (DoS), Distributed DoS (DDoS)
	- **Sfruttamento di bugs nel software installato (System Integrity and Authentication attacks):**
		- Applicazione degli Exploit noti
	- **Diffusione di Vulnerabilità intenzionali (System Integrity attacks):** 
		- Virus, Worms, BOT, Trojan
	- **Ingegneria Sociale:**
		- Phishing

### Attacco passivo
#### Sniffing e Scanning
- **Sniffing**: analizzare il traffico di rete utilizzando un analizzatore di protocollo, è necessario un accesso privilegiato all'interfaccia di rete. 
    Possono essere orientati ad analizzare una sequenza di pacchetti
	- Esempi di strumenti: tcpdump e wireshark.
- **Scanning**: testare un intervallo di indirizzi IP e numeri di porta per vedere quali servizi o sistemi sono presenti ed attivi.
	- Esempio di strumento : nmap → è uno tool open-source per la network exploration e l'auditing.

### Attacco Attivo
#### Spoofing (fabbricazione)
E' un tipo di attacco informatico dove viene impiegata la falsificazione dell'identità (spoof), quando la falsificazione non avviene in campo informatico si parla di social engineering.
- **User account spoofing**: usare nome utente e password di un altro utente senza averne il diritto, può avvenire utilizzando strumenti come sniffer e password crackers, i password cracker possono essere off-line come John the Ripper, oppure on-line, come Hydra.
- **IP Address spoofing**: Si basa sul fatto che la maggior parte dei routers all'interno di una rete controllino solo l'indirizzo IP di destinazione e non quello sorgente
    Finalità:
	- superare le tecniche difensive basate sull'autenticazione dell'indirizzo.
	- Realizzare attacchi DDoS. Vedi ad esempio “NTP reflection”.
- **MAC Address forging**: il MAC address viene modificato impersonando l'indirizzo della vittima, diversi sistemi di autenticazione/autorizzazione sono basati su MAC address.
	- Autenticazione verso DHCP server.
	- Sessioni attive su Captive Portal (session Hijacking).
- **ARP Spoofing / Poisoning**: consiste nell'inviare intenzionalmente e in modo forzato risposte ARP contenenti dati inesatti, in questo modo la tabella ARP di un host conterrà dati alterati. Ettercap è un tool per attacco di tipo man-in-the-middle, basato su ARP poisoning.

#### DoS - Denial of Service
Mira a impedire legittimo accesso o utilizzo di risorse da parte degli utenti autorizzati sovraccaricando o intasando un sistema, un'applicazione o una rete. È importante notare che nella maggior parte degli attacchi DoS, l'obiettivo principale è impedire l'accesso o l'utilizzo delle risorse piuttosto che consentire l'accesso all'attaccante.
- diretti (l’attaccante interagisce direttamente con la vittima).
- indiretti (l’attacante sfrutta terze parti).

Principali attacchi:
- **Flooding**
	- Ping floods: invio di ICMP echo request in numero maggiore a quelli gestibili dal sistema attaccato; l’aggressore invia un grosso flusso di traffico ICMP echo verso una serie di indirizzi di broadcast attribuendosi come indirizzo sorgente quello della vittima.
	- TCP SYN Floods: funziona se un server alloca delle risorse dopo aver ricevuto un SYN, ma prima di aver ricevuto un messaggio ACK (vedi nmap -sS).
- **Invio di pacchetti malformati**
	- Ping di grandi dimensioni (ping of death): può causare buffer overflow con conseguente blocco del servizio o, nei casi più gravi, crash del sistema.
	- UDP bombs: costruiti con valori illegali in certi campi. In certi sistemi operativi la ricezione di pacchetti imprevisti può causare crash.
- **Attacchi da più host**: DDOS (Distributed DoS) è una variante di DoS realizzato utilizzando numerose macchine attaccanti che insieme costituiscono una “botnet” controllate da un una unica entità, il botmaster.

#### Gli Exploit
La vulnerabilità può essere intesa come una componente di un sistema, in corrispondenza alla quale le misure di sicurezza sono assenti, ridotte o compromesse, il che rappresenta un punto debole del sistema e consente a un eventuale aggressore di compromettere il livello di sicurezza dell'intero sistema.
La vulnerabilità si presenta ovunque ci sia un difetto di progettazione, codifica, installazione e configurazione del software, un **exploit** è un frammento di codice, una sequenza di comandi, o un insieme di dati, che prendono vantaggio da una vulnerabilità per acquisire privilegi di accesso, eseguire codice o creare DoS su di una risorsa.

I più comuni tipi di exploit prendono vantaggio da:
- **Buffer overflow** (Stack o Heap): si basa sul fatto che un programma potrebbe non controllare in anticipo la lunghezza dei dati in arrivo, ma si limita a scrivere il loro valore in un buffer di lunghezza prestabilita, confidando che l'utente (o il mittente) non immetta più dati di quanti esso ne possa contenere.
- **Code injection**: Questo exploit sfrutta l'inefficienza dei controlli sui dati ricevuti in input ed inserisce codice maligno (ad esempio all'interno di una query SQL, oppure attraverso Remote File Inclusion) 
Spesso, quando gli exploit vengono pubblicati, la vulnerabilità viene eliminata attraverso una Patch che produce una nuova versione del software.

#### Malware
Un qualsiasi software creato allo scopo di causare danni a un computer, ai dati degli utenti del computer, o a un sistema informatico su cui viene eseguito.
- **Virus**: sono parti di codice che si diffondono copiandosi all'interno di altri programmi, o in una particolare sezione del disco fisso, in modo da essere eseguiti ogni volta che il file infetto viene aperto.
- **Worm**: questi malware non hanno bisogno di infettare altri file per diffondersi, perché modificano il sistema operativo della macchina ospite in modo da essere eseguiti automaticamente e tentare di replicarsi sfruttando per lo più Internet.
- **Trojan**: software che oltre ad avere delle funzionalità "lecite", utili per indurre l'utente ad utilizzarli, contengono istruzioni dannose che vengono eseguite all'insaputa dell'utilizzatore.
- **Spyware**: software che vengono usati per raccogliere informazioni dal sistema su cui sono installati e per trasmetterle ad un destinatario interessato.

#### Ingegneria sociale e Spam
- **Ingegneria sociale**: lo studio del comportamento individuale di una persona al fine di carpire informazioni utili.
	- Phishing: è un tipo di ingegneria sociale attraverso la quale un aggressore cerca di ingannare la vittima convincendola a fornire informazioni personali sensibili.
- **Spam**: lo spamming è l'invio di messaggi indesiderati (generalmente commerciali), può essere attuato attraverso qualunque sistema di comunicazione, ma il più usato è Internet, attraverso messaggi di posta elettronica.
	- Più dell'80% delle email inviate oggi nel mondo è Spam.
	- Il termine SPAM deriva dai Monty Python.

## Strumenti di difesa
- **Dominio di Sicurezza:** rappresenta un'area amministrativa o operativa in cui risorse e entità simili sono gestite in conformità con regole di sicurezza condivise. Ad esempio, un'organizzazione può avere diversi domini di sicurezza, ognuno con le proprie politiche e regolamenti specifici
- **Perimetro di Sicurezza:** rappresenta il confine tra l'ambiente interno e esterno di un dominio di sicurezza. È la zona dove le misure di sicurezza sono particolarmente rafforzate per proteggere l'accesso non autorizzato da parte di entità esterne. Questo può includere firewall, sistemi di rilevamento degli intrusi e altri dispositivi di sicurezza.
- **Superficie di Attacco:** è costituita dai vari punti in cui un attaccante potrebbe cercare di compromettere la sicurezza di un sistema o di un'organizzazione. Ridurre la superficie di attacco implica implementare misure di sicurezza per limitare i punti di accesso potenziali, riducendo così le opportunità per gli attaccanti di sfruttare vulnerabilità. Ciò include l'implementazione di patch regolari, la configurazione sicura dei servizi e l'adozione di best practice di sicurezza.
### Domini di Sicurezza
- **Assegnazione di Grado di Fiducia:** ogni dominio di sicurezza riceve una classificazione o grado di fiducia che riflette il suo livello di sicurezza e il suo rapporto con altri domini.
- **Regole di Visibilità:** determinano quali domini possono vedere o interagire con altri. Queste regole sono basate sui gradi di fiducia assegnati.
    Un dominio con un grado di fiducia più elevato può avere accesso più ampio, mentre un dominio con un grado più basso può avere un accesso limitato.
- **Eccezioni alle Regole di Visibilità:** possono essere definite per consentire specifiche interazioni tra domini con gradi di fiducia diversi.
    Ad esempio, la DMZ e l'INSIDE possono avere una visibilità completa sull'OUTSIDE, ma l'accesso tra altri domini può essere limitato o bloccato.

Nell'esempio fornito, la DMZ e l'INSIDE hanno una visibilità completa sull'OUTSIDE, la DMZ è una zona intermedia tra l'ambiente interno e quello esterno e spesso contiene servizi o risorse accessibili dall'esterno senza compromettere la sicurezza interna.

![[securety_domains.png]]

>Questo modello di classificazione e regolamentazione dei gradi di fiducia e visibilità è fondamentale per stabilire una gerarchia di sicurezza e garantire che l'accesso a risorse sensibili sia controllato e limitato in modo appropriato.

### Architettura di Base della Sicurezza
In un'architettura di rete comune ci sono almeno tre domini:
- **Esterno (tutto il mondo esterno - Internet)**: Rappresenta tutto ciò che si trova al di fuori dell'organizzazione, inclusa l'ampia area di Internet. Il grado di fiducia è 0, indicando che non c'è alcuna fiducia implicita nelle risorse esterne.
- **Interno (l'organizzazione interna da proteggere e nascondere)**: Questo è l'ambiente interno dell'organizzazione che richiede la massima protezione. Il grado di fiducia è al massimo, pari a 100, indicando un elevato livello di fiducia nelle risorse interne.
- **DMZ (insieme di macchine interne che espongono servizi all'esterno)**: La DMZ è una zona intermedia tra l'ambiente interno e quello esterno. Contiene macchine che forniscono servizi accessibili dall'esterno. Il grado di fiducia è compreso tra 0 e 100, indicando che la fiducia in quest'area è moderata e varia a seconda della necessità di esposizione dei servizi.

Questo modello a tre domini riflette la pratica comune di dividere una rete in zone con diversi livelli di fiducia, contribuendo a proteggere le risorse più sensibili dall'accesso non autorizzato proveniente dall'esterno.

![[architettura_sicurezza.png]]

#### Firewall
Per firewall si intende una entità hardware o software che si pone tra internet e la rete (o l'host ) che si vuole proteggere.
Il firewall svolge una funzione di filtro, consentendo il transito solamente alle connessioni ritenute lecite mediante una opportuna “Policy”. 
Obiettivi principali:
- Monitorare, limitare, autenticare l'accesso alla rete da proteggere nei confronti di accessi provenienti dall'esterno (Internet).
- Monitorare, limitare, autenticare l'accesso all'esterno (Internet) da parte dell'utenza interna.
I firewall possono essere di 2 tipi: 
- I packet filter: agiscono ai livelli 3 e 4.
- I proxy: agiscono a livello applicazione.

![[firewall.png]]

##### Firewall: packet filter
Questo filtro analizza tutti i pacchetti in transito e applica azioni del tipo permit/deny sulla base di politiche basate sugli indirizzi IP e le porte di provenienza e/o di destinazione. 
Obiettivi:
- Rendere visibili ad internet solamente i servizi di rete destinati ad un accesso pubblico (protezione dei servizi intranet e dei servizi “inconsapevoli”)
- Bloccare il traffico indesiderato (es: P2P, ..) 
- Strumento per la gestione delle emergenze (bloccare un host ostile o contaminato da virus).
Agisce a livello di pacchetti IP, ma deve leggere anche i primi byte del livello 4 per leggere le porte TCP o UDP. 
Può essere realizzato dai Router mediante un modulo aggiuntivo o da HW specifico. Per Linux esiste il modulo IPtables che può essere applicato ad una interfaccia di rete.
##### Firewall: proxy
Il **proxy** è un intermediario tra un client e un server, agendo come un tramite che facilita la comunicazione tra di essi. Il client, che potrebbe essere un utente o un'applicazione, invia le sue richieste al proxy invece di connettersi direttamente al server di destinazione. Il proxy quindi inoltra la richiesta al server e restituisce la risposta al client. Questa interazione può avvenire in modo implicito o esplicito, a seconda della configurazione del sistema.

Obiettivi:
- **Mettere in comunicazione client e server che non hanno visibilità diretta** (ad esempio se il client è in una rete intranet).
- **Migliorare le prestazioni**: quando un client richiede una risorsa già presente nella cache del proxy, questa viene fornita direttamente dal proxy anziché dal server, riducendo i tempi di risposta e il carico sulla rete (es: Web Caching).
- **Servizi di sicurezza**:
	- Auditing (tracciamento delle attività) 
	- Autenticazione e Autorizzazione
- **Controllo degli Accessi e Filtraggio**: possono essere configurati per controllare e filtrare l'accesso a determinati siti web o contenuti, garantendo la conformità alle politiche aziendali o di sicurezza.
- **Nascondere l'Identità del Cliente**: possono nascondere l'identità del cliente agli occhi del server, fornendo un certo grado di anonimato durante la navigazione su Internet.
- **Ottimizzazione del Traffico di Rete**: riducendo la quantità di dati scambiati tra client e server attraverso tecniche come la compressione o la riduzione del numero di richieste.
#### ACL - Access Control List sul Router
Il router è un apparato di rete posto solitamente tra LAN e internet, che svolge il compito di gestione dei singoli pacchetti per il loro instradamento, la gran parte dei router possono essere configurati per svolgere anche la funzionalità di Packet filter. 
Il sistema operativo IOS dei router Cisco consente la definizione di ACL (Access Control List), una lista di regole che specifica quali pacchetti di rete sono autorizzati (consentiti) o negati (bloccati) in base a determinati criteri come indirizzi IP, porte, protocolli e altre caratteristiche, che possono essere applicate alle interfacce del router. 

In questo esempio viene creata una ACL sul traffico entrante che consente l'accesso ai soli server WEB ed EMAIL, bloccando il resto. L'ACL è poi applicata all'interfaccia opportuna.

```Terminale
access-list 140 permit tcp any host "webserver" eq www 
access-list 140 permit tcp any host "mailserver" eq smtp 
access-list 140 permit tcp any host "mailserver" eq pop3 
access-list 140 permit tcp any host "mailserver" eq imap 
access-list 140 deny ip any any log 

interface eth 0 
	ip access-group 140 in
```

#### IPtables
Il pacchetto software IPtables consente di applicare ACL per il Packet filtering sulle interfacce di Sistemi Linux. 
IPtables lavora sulle 3 tabelle: filter, nat, mangle, sulle quali possiamo creare catene  (chains) di regole ACL. 

La tabella **Filter** (tabella di default) server per il packet filter.
Le tabelle **NAT** (SNAT e DNAT) servono per le regole di NATting.
La tabella **Mangle** serve per modificare alcuni parametri nell'header pacchetto 

La tabella Filter ha 3 catene di Default applicate su una interfaccia di rete:
- INPUT per il processamento dei pacchetti destinati all'host.
- OUTPUT per i pacchetti provenienti dall'host.
- FORWARD per i pacchetti che devono attraversare il firewall.

### Antivirus
è un software atto a prevenire, rilevare ed eventualmente eliminare programmi dannosi, ha anche una funzione preventiva, impedendo che un virus possa entrare in un sistema ed infettarlo. 
Il metodo più utilizzato per individuare virus in un file è attraverso le signatures (firma), il programma AV calcola la firma (signature) di un file da analizzare (e.g. Hash MD5 dell'intero file ) e lo confronta con le firme di virus noti presenti all'interno di un archivio, se la firma corrisponde il file è sicuramente un virus.
Esistono anche tecniche euristiche, di solito usate in modo complementare alle firme, che cercano di individuare virus non noti all'AV attraverso la ricerca di pattern sospetti. 

Può essere installato:
- sul PC: scan dei dischi dell'host e dei nuovi file salvati 
- sul MailServer: scan delle mail in entrata e in uscita 

### Tecniche Antispam
- **Black list**: lista di server classificati spammers che viene attivata sul mail server rifiutando mail che provengono da host inclusi in questa lista. 
    L'amministratore del mailserver può costruire manualmente una propria lista o può avvalersi di servizi in Internet che distribuiscono automaticamente le liste. 
- **Gray-List**: si basano sul fatto che i mailer usati dagli spammer generalmente tentano l'invio di una email una sola volta: Il GrayListing consiste nel rigetto della ricezione della mail al primo tentativo, che verrà accettata ad un successivo tentativo, dopo un tempo stabilito (tipicamente 300 sec.) 
- **White List**: liste di mittenti “Fidati” su cui non vengono effettuati controlli antispam. Include gli host accettati da Gray-list e host inseriti manualmente dall'amministratore. 
- **Filtri Bayesiani**: sono filtri che cercano di classificare le mail in arrivo assegnando un punteggio numerico a frasi o modelli che si presentano nel messaggio. Ogni messaggio riceve quindi un punteggio compressivo (tra 0 e 1) che, dopo aver stabilito una soglia, ci consente di classificare il messaggio. Il filtro richiede un addestramento con mail spam e no-spam con cui viene creato un database di riferimento.

### Auditing di sicurezza informatica
Un **audit** di sicurezza informatica è un’analisi sistematica con l’obiettivo di verificare i controlli di sicurezza, politiche e procedure in atto e convalidare il loro efficace funzionamento in base al rischio. 
Gli elementi oggetto di valutazione di un audit di sicurezza informatica sono: 
- **personale aziendale**, ovvero le modalità utilizzate dai dipendenti per raccogliere, condividere e archiviare informazioni sensibili. 
- I componenti del **sistema informatico** e ambiente in cui è ospitato 
- **applicazioni e software** (incluse le patch di sicurezza messe a punto dagli amministratori di sistema) 
- **vulnerabilità della rete** interna ed esterna 

**Passaggi principali dell’auditing:** 
- Definizione degli asset: elenco dettagliato di risorse, dati sensibili, apparecchiature informatiche e relativa valutazione del rischio informatico.
- Valutazione del personale.
- Monitoraggio dei sistemi e delle reti.
- Identificazione delle vulnerabilità.
- Risposte al rischio, aumento delle protezioni.

#### Audit del personale
La sicurezza dei sistemi e delle reti dipende anche dal comportamento degli utenti e degli amministratori di sistema. Occorre annotare e registrare quali dipendenti abbiano accesso alle informazioni sensibili e quanti di loro siano preparati in maniera adeguata. 

Il rischio principale riguarda il **furto delle credenziali per l’accesso ai sistemi aziendali**, la password è una delle forme di identificazione più semplici ed utilizzate ed è quindi uno dei principali bersagli degli attacchi. 
I metodi più utilizzati sono: 
1) Intercettazione: l'utilizzo di un canale non cifrato consente la cattura delle password sulla rete. 
2) Furto: alcuni utenti tendono a scriverla su un supporto magnetico per non dimenticarla. 
3) Tentativi di indovinare la password (password cracker basati su dizionari) 
4) Phishing.

I risultati dell’audit sul personale vengono utilizzati per programmare un **piano di formazione del personale.**

#### Auditing di sistema
L’audit di sicurezza informatica richiede la definizione dell’elenco dei sistemi, la loro classificazione in base al rischio informatico e l’attribuzione del ruolo di amministratore. L’amministratore di sistema deve definire un programma di audit attraverso il quale viene definita la gestione e l'analisi degli eventi, con i seguenti obiettivi: 
- (Early) warning: Individuare rapidamente eventuali attacchi in corso. 
- Trouble-shooting: mantenere uno storico degli eventi per tracciare le attività. 

**rsyslog** è lo strumento base per l’audit di sistema in ambiente Linux, consente ai processi interni di generare eventi classificati in categorie ( KERN, USER, MAIL, DAEMON, AUTH, LPR, CRON, LOCAL0-7) e priorità ( EMERG, ALERT, CRIT, ERR, WARNING, NOTICE, INFO, DEBUG). 
Per ogni evento è possibile definire una azione come scrivere su file (tipicamente nella directory /var/log) , inviare mail o attivare script.

#### Audit della rete
Consiste nella raccolta e analisi sistematica del traffico di rete e per la rilevazione in tempo reale di minacce provenienti dalla rete, è necessaria la nomina di un amministratore di rete. 
Strumenti utili sono i **Network Monitor** (esempio ntop , dotato di una console web), gli **Intrusion Detection Systems** (IDS), gli **Honeypot** e i **Vulnerability Scanners.**

##### IDS - intrusion Detection System
IDS è un dispositivo software/hardware per identificare accessi non autorizzati a host o LAN. 
L'IDS generalmente si appoggia su un Data-Base per memorizzare le regole utilizzate per individuare le violazioni di sicurezza, sono classificabili nel seguente modo: 
- Host IDS (HIDS): analizzano file di log e file system sull'Host. 
	- TRIPWIRE è un esempio di HIDS, si basa sulla differenza tra lo stato analizzato ed uno stato iniziale. 
- Network IDS (NIDS): analizzano il traffico di rete. 
	- SNORT è un esempio di NIDS che può funzionare anche come sniffer/packet logger. 

Quando un IDS rileva una intrusione invia una notifica all'amministratore via e-mail o con un messaggio alla console (continuous monitoring e auditing).

###### IPS - Intrusion Prevention System
Gli IPS sono un'estensione degli strumenti di IDS: quando rilevano un tentativo di intrusione sono abilitati a bloccare gli accessi considerati pericolosi. 
IPS può mandare un allarme (come un IDS), ma anche interagire con un firewall per eliminare pacchetti malevoli, resettare le connessioni e/o bloccare il traffico da un indirizzo IP attaccante. 
Strumenti utili: **fail2ban** è pensato per prevenire attacchi “brute force” via ssh bloccando temporaneamente gli indirizzi IP che provano a violare la sicurezza di un sistema. 
Il programma effettua il parsing di alcuni file di log che contengono informazioni relative ad accessi falliti, se il numero di accessi falliti supera una certa soglia l’indirizzo IP del client viene bloccato attraverso una regola di iptables.

##### Honeypot
Un **honeypot** è un sistema o componente hardware o software usato come "trappola" o "esca" a fini di protezione contro gli attacchi. 
Consiste in un computer o un sito che sembra essere parte della rete, ma che in realtà è ben isolato e non ha contenuti sensibili o critici. Consente di rilevare attività malevole senza coinvolgere la rete interna.

![[honeypot.png]]

##### Identificazione delle vulnerabilità 
Un **vulnerability scanner** è un programma progettato per ricercare e mappare le debolezze di un singolo computer o degli host di una rete. 
Identifica le vulnerabilità dovute a software con bugs o non aggiornato, configurazioni errate all’interno di servizi applicativi, web server, firewall router, ecc 
Scanner più utilizzati: **Nessus** (commerciale) e **openVAS** (opensource). 
Funzionamento: 
1. ricerca host attivi.
2. port scanning per ogni host.
3. ricerca vulnerabilità tramite test non invasivi.
4. identificazione vulnerabilità tramite confronto con database.
5. generazione di un report.

### Vulnerabilità: Dizionari e Alert
Le vulnerabilità note vengono censite in dizionari da organizzazioni internazionali, indicando il software interessato, l’impatto e i rimedi da applicare. 
Il dizionario più noto è il «Common Vulnerabilities and Exposures» (CVE) mantenuto dalla MITRE Corporation e finanziato dal Dipartimento della Sicurezza interna degli Stati Uniti. 
La severità delle vulnerabilità è misurata con «Common Vulnerability Scoring System” (CVSS) che assegna ad ogni vulnerabilità un punteggio tra 0 e 10.
Diverse organizzazioni pubblicano quotidianamente le nuove vulnerabilità attraverso «Vulnerability Alert».
Alcune organizzazioni forniscono strumenti per il Vulnerability scanning.

### CERT - Computer Emergency Response Team
Un CERT (o CSIRT – Computer Security Incident Response Team) è un Servizio offerto all'interno di una comunità di utenti Internet per la gestione di emergenze in seguito ad attacchi informatici. 
L’assistenza tecnica avviene attuando piani immediati di incident response in caso di attacco e attraverso la massiccia diffusione di informazioni per la prevenzione di incidenti informatici.

### Standard e normative di sicurezza informatica
Gli standard di sicurezza informatica sono metodologie che permettono alle organizzazioni di attuare tecniche di sicurezza finalizzate a minimizzare la quantità e la pericolosità delle minacce alla sicurezza informatica. 

**Normative per la sicurezza informatica** 
Uno degli standard di sicurezza più ampiamente utilizzato è l’ISO 27001 del 2013 che include un elenco di 114 controlli e che prevede una certificazione per le aziende. Nel 2017 AGID (Agenzia per l’Italia Digitale) ha emanato le «Misure minime di sicurezza ICT» che le pubbliche amministrazioni devono adottare.

**Normative per la protezione dei dati**
Nel 2016 l’Agenzia dell’Unione Europea per la Cybersecurity, ENISA, ha emanato il regolamento generale sulla protezione dei dati (GDPR), adottato in Italia attraverso un regolamento emanato dal «Garante per la protezione dei dati personali» a cui si deve attenere chi tratta i dati personali. L’articolo 34 descrive le misure minime da adottare in caso di trattamento di dati personali con strumenti elettronici.