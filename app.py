import random
import streamlit as st

st.set_page_config(
    page_title="Forenzička biologija | Obnavljanje gradiva",
    page_icon="🧬",
    layout="wide",
)

st.title("🧬 Forenzička biologija 2026/27")
st.caption("Prirodno-matematički fakultet u Nišu, Departman za Biologiju i ekologiju")

st.markdown(
    """
    Izaberite karticu za **predavanje** ili **vežbu**. U svakoj lekciji
    nalaze se sažetak ključnih pojmova i 20 pitanja sa ponuđenim odgovorima.
    Na kraju kviza dobijate broj tačnih odgovora i objašnjenja.
    """
)

LECTURE_SUMMARY = """
### 1. Forenzičke nauke i značaj forenzičke genetike
Forenzičke nauke prikupljaju, obrađuju i tumače informacije iz prošlosti kako bi se izveli
zaključci o događaju. Forenzička genetika koristi genetičke informacije za povezivanje
osumnjičenih sa dokaznim tragovima, identifikaciju žrtava, rešavanje sporova oko roditeljstva
i istorijska istraživanja, uključujući proučavanje migracija.

### 2. Otkriće i istorija DNK
- **1866.** Gregor Mendel postavlja temelje moderne genetike postuliranjem naslednih faktora.
- **1869.** Friedrich Miescher izoluje nuklein iz leukocita; Richard Altmann 1889. uvodi naziv
  „nukleinska kiselina“.
- **1909.** Wilhelm Johannsen uvodi naziv „gen“.
- **1910-e.** Thomas Hunt Morgan pruža dokaze da su geni fizički entiteti smešteni na hromozomima.
- **1928.** Frederick Griffith otkriva bakterijsku transformaciju.
- **1944.** Oswald Avery i saradnici identifikuju DNK kao aktivnu komponentu transformišućeg ekstrakta.
- **1952.** Hershey i Chase eksperimentima sa bakteriofagom T2 potvrđuju ulogu DNK kao naslednog materijala.
- **25. april 1953.** Watson i Crick objavljuju model sekundarne strukture DNK. Danas se 25. april obeležava
  kao Dan DNK; projekat Genom čoveka završen je 2003. godine.

### 3. Hemijska struktura DNK
Nukleotid čine fosfatna grupa, pentoza i azotna baza. U DNK je šećer dezoksiriboza, a baze su
adenin (A), guanin (G), citozin (C) i timin (T). Purinske baze su A i G, a pirimidinske C i T.
U RNK je riboza, a uracil zamenjuje timin. Prema Šargafovom pravilu, u dvolančanoj DNK važi
A = T i G = C, odnosno ukupna količina purina jednaka je količini pirimidina.

### 4. Ključni doprinosi razumevanju strukture
Difrakcija X-zraka doprinela je razumevanju strukture DNK. U radu su učestvovali Maurice Wilkins,
Rosalind Franklin i Raymond Gosling; poznata „Fotografija 51“ povezana je sa radom Franklin i Goslinga.

### 5. Centralna dogma
Genetička informacija se uobičajeno prenosi od nukleinske kiseline ka proteinima. Centralna dogma
naglašava da se informacija ne prenosi iz proteina nazad u nukleinsku kiselinu.

### 6. Razvoj forenzičkog DNK profilisanja
- RFLP analiza koristi restrikcione enzime za sečenje DNK na specifičnim mestima i poređenje dužina fragmenata.
- Alec Jeffreys je 1985. razvio DNK „fingerprinting“ zasnovan na varijabilnim VNTR/minisatelitnim regionima,
  uz Southern blot i hibridizaciju sa DNK probama.
- PCR je omogućio umnožavanje ciljnih sekvenci iz malih količina i degradiranih uzoraka.
- STR (Short Tandem Repeats) markeri su kraći od VNTR lokusa i pogodni za PCR amplifikaciju, zbog čega su
  postali važni u rutinskom forenzičkom profilisanju.

### 7. Veza sa molekularnogenetičkom analizom tragova (udžbenik, poglavlje 3)
Analiza DNK iz biološkog traga obuhvata izolaciju, procenu količine i kvaliteta DNK, umnožavanje STR markera
i generisanje/interpretaciju DNK profila. Izolacija uključuje lizu ćelija, purifikaciju lizata i prikupljanje DNK.
U lizi se mogu koristiti deterdženti (npr. SDS), EDTA i proteinaza K. Purifikacija uklanja proteine i druge
kontaminante; DNK se zatim može isprati, osušiti i rastvoriti u vodi ili TE puferu.

Za izolaciju se koriste organske metode, Chelex/isoljavanje i komercijalni setovi zasnovani, između ostalog,
na silika-membranama ili magnetnoj separaciji. Kvantifikacija je važna pre amplifikacije. UV spektrofotometrija
i gel-elektroforeza mere ukupnu DNK, ali nisu specifične za humanu DNK. Fluorometrija je osetljivija, ali
takođe ne razlikuje ljudsku od DNK drugih organizama. Real-time PCR omogućava osetljivu kvantifikaciju
humane DNK, može ukazati na degradaciju i prisustvo inhibitora.
"""

EXERCISE_SUMMARY = """
### 1. Mesto zločina
Mesto zločina obuhvata mesto izvršenja radnje, mesto nastupanja posledice i svako drugo mesto na kome
se nalaze predmeti ili tragovi relevantni za dokazivanje. Može biti primarno, sekundarno ili tercijarno.
Može biti netaknuto ili izmenjeno; izmenjeno mesto može biti inscenirano ili preuređeno. Mesto se može
posmatrati i kao mikro- ili makrolokacija.

### 2. Tragovi
Trag je materijalna promena nastala izvršenjem krivičnog dela, koja sadrži informacije o poreklu ili uzroku.
Tragovi mogu pomoći u utvrđivanju gde i kada se događaj odigrao, kako je tekao, ko je učestvovao,
čime je delo izvršeno i, potencijalno, motiva. Traseologija je nauka o tragovima.

Tragovi se razvrstavaju prema:
- uočljivosti: vidljivi golim okom ili teško/nevidljivi;
- veličini: makro- i mikrotragovi;
- izgledu: reljefni i površinski;
- poreklu: ljudski, biljni, životinjski, tragovi predmeta, sile, požara ili eksplozije;
- vrsti: fizički, hemijski i biološki.

### 3. Obezbeđenje lica mesta i uviđaj
Obezbeđenje lica mesta podrazumeva mere kojima se mesto i tragovi čuvaju od izmena do obrade.
Uviđaj je hitna istražna radnja koja se preduzima kada je neposredno opažanje potrebno za utvrđivanje
ili razjašnjenje važne činjenice. Potrebno je odrediti granice, ograničiti pristup i sačuvati tragove.
Prema materijalu sa vežbi, uviđaj nije obavezan i sprovodi se na osnovu odluke organa koji vodi postupak.

### 4. Faze obrade lica mesta
- **Informativna/verbalna faza:** prikupljanje informacija razgovorom sa svedocima i drugim licima.
- **Statička faza:** obezbeđenje i pregled mesta, opažanje, identifikacija, označavanje, merenje,
  opisivanje i fotografisanje tragova; predmeti se ne dodiruju i ne pomeraju.
- **Dinamička faza:** analiza, fiksiranje, osiguranje, prikupljanje i bezbedno pakovanje tragova i predmeta.

### 5. Dokumentovanje i rekonstrukcija
Obrada obuhvata intervju, fotodokumentaciju, skicu, pronalaženje i fiksiranje tragova, kao i zapisnike
i izveštaje. Fotografije treba da prikažu mesto u odnosu na okolinu, kao i detalje sa veće, srednje i male
udaljenosti; može se koristiti koso osvetljenje. Skica prikazuje izgled lica mesta i položaj žrtve/dokaza.
Rekonstrukcija se izuzetno sprovodi, između ostalog, kada nova saznanja ili novi tragovi nisu u skladu
sa zatečenim stanjem; zasniva se na fizičkim dokazima i predstavlja metodičan proces.

### 6. Fizički i biološki dokazi
Fizički dokaz je predmet koji može povezati žrtvu ili osumnjičenog sa mestom zločina. Obuhvata dokaze
u tragovima, biološke dokaze i uporedne dokaze. Biološki tragovi mogu poticati od ljudi, životinja ili biljaka.
Ljudski biološki tragovi uključuju delove tela, zube, dlake, nokte, krv i telesne izlučevine.

U materijalu sa vežbi biološki tragovi su grupisani prema potencijalu (broju molekula DNK po jedinici
zapremine): I grupa — sperma i tkiva; II — krv (leukociti); III — pljuvačka i sekret iz nosa; IV — epitelne
ćelije kože. Tragovi se otkrivaju vizuelnim pregledom, alternativnim izvorima svetlosti i hemijskim reagensima.
Biološki dokazi se smatraju potencijalno zaraznim, a ograničavanje broja prisutnih na mestu događaja
smanjuje mogućnost kontaminacije.
"""

# Each item: question, options, correct option index, explanation
LECTURE_QUESTIONS = [
("Šta je osnovni zadatak forenzičkih nauka?", [
    "Da prikupljaju, obrađuju i tumače informacije iz prošlosti radi izvođenja zaključaka",
    "Da utvrđuju samo identitet živih osoba",
    "Da proučavaju isključivo uzroke bolesti",
    "Da čuvaju biološke uzorke bez njihove analize"], 0,
 "Forenzičke nauke obrađuju informacije i tragove kako bi se izveli zaključci o događaju."),
("Koji je primer primene forenzičke genetike naveden u predavanju?", [
    "Povezivanje osumnjičenog sa dokaznim tragovima",
    "Određivanje starosti fosila isključivo na osnovu izgleda",
    "Merenje brzine vetra na mestu događaja",
    "Utvrđivanje hemijskog sastava zemljišta bez bioloških uzoraka"], 0,
 "Predavanje navodi rasvetljavanje zločina povezivanjem osumnjičenih sa dokaznim tragovima."),
("Ko je 1866. postulirao postojanje naslednih faktora?", [
    "Gregor Mendel", "Wilhelm Johannsen", "Thomas Hunt Morgan", "Friedrich Miescher"], 0,
 "Mendel je postavio temelje moderne genetike postuliranjem naslednih faktora."),
("Ko je uveo naziv „gen“ 1909. godine?", [
    "Wilhelm Johannsen", "Oswald Avery", "Alfred Hershey", "James Watson"], 0,
 "Naziv „gen“ pripisuje se danskom naučniku Wilhelmu Johannsenu."),
("Ko je prvi izolovao nukleinske kiseline i nazvao izolovani materijal nuklein?", [
    "Friedrich Miescher", "Richard Altmann", "Rosalind Franklin", "Frederick Griffith"], 0,
 "Miescher je 1869. izolovao nuklein iz materijala bogatog leukocitima."),
("Šta je otkrio Frederick Griffith 1928. godine?", [
    "Fenomen bakterijske transformacije",
    "Strukturu dvostruke spirale DNK",
    "PCR metodu",
    "STR markere"], 0,
 "Griffith je u eksperimentima sa Streptococcus pneumoniae opisao transformaciju."),
("Koji je zaključak proistekao iz eksperimenata Averyja i saradnika iz 1944?", [
    "DNK je aktivna komponenta transformišućeg ekstrakta",
    "Proteini su jedini nosioci nasledne informacije",
    "RNK se ne nalazi u ćeliji",
    "Hromozomi nisu povezani sa nasleđivanjem"], 0,
 "Avery i saradnici identifikovali su DNK kao aktivnu komponentu koja izaziva transformaciju bakterija."),
("Na kom organizmu/sistemu su Hershey i Chase 1952. izvodili eksperimente?", [
    "Bakteriofagu T2", "Drosophila melanogaster", "Caenorhabditis elegans", "Escherichia coli bez faga"], 0,
 "Eksperimenti sa bakteriofagom T2 potvrdili su ulogu DNK kao naslednog materijala."),
("Koje godine je objavljen rad Watsona i Cricka o strukturi DNK?", [
    "1953.", "1944.", "1952.", "1969."], 0,
 "Rad je objavljen 25. aprila 1953. u časopisu Nature."),
("Od kojih komponenti se sastoji nukleotid DNK?", [
    "Fosfatne grupe, dezoksiriboze i azotne baze",
    "Aminokiseline, glukoze i fosfolipida",
    "Riboze, proteina i masne kiseline",
    "Samo azotne baze i proteina"], 0,
 "Nukleotid DNK sadrži fosfat, pentozu (dezoksiribozu) i azotnu bazu."),
("Koje baze su purinske baze u DNK?", [
    "Adenin i guanin", "Citozin i timin", "Adenin i timin", "Guanin i citozin"], 0,
 "Adenin (A) i guanin (G) su purini; citozin i timin su pirimidini."),
("Koja baza u RNK zamenjuje timin?", [
    "Uracil", "Guanin", "Adenin", "Citozin"], 0,
 "U RNK se umesto timina nalazi uracil."),
("Šta prema Šargafovom pravilu važi za dvolančanu DNK?", [
    "A = T i G = C", "A = G i T = C", "A = C i G = T", "Sve četiri baze su uvek zastupljene jednako"], 0,
 "U dvolančanoj DNK količina adenina odgovara količini timina, a guanina količini citozina."),
("Sa kojim naučnicima je u predavanju povezana „Fotografija 51“?", [
    "Rosalind Franklin i Raymond Gosling",
    "Watson i Crick",
    "Mendel i Morgan",
    "Avery i Griffith"], 0,
 "Fotografija 51 povezana je sa difrakcionim radom Rosalind Franklin i njenog doktoranda Raymonda Goslinga."),
("Šta opisuje centralna dogma molekularne biologije?", [
    "Prenos genetičke informacije od nukleinskih kiselina ka proteinima, a ne obrnuto",
    "Prenos informacije od proteina ka DNK",
    "Prevođenje proteina u RNK",
    "Nasumičnu promenu redosleda nukleotida"], 0,
 "Centralna dogma opisuje smer prenosa informacije od nukleinske kiseline ka proteinu."),
("Na čemu se zasniva RFLP analiza?", [
    "Sečenju DNK restrikcionim enzimima i poređenju dužina fragmenata",
    "Direktnom određivanju aminokiselinskog niza",
    "Merenju ukupnog broja ćelija",
    "Vizuelnom poređenju fenotipa"], 0,
 "RFLP koristi restrikcione enzime; varijacije u dužini fragmenata mogu ukazati na genetičke razlike."),
("Koji pristup je Alec Jeffreys koristio za prvi DNK fingerprinting?", [
    "VNTR/minisatelitne lokuse, Southern blot i hibridizaciju DNK probama",
    "Samo mikroskopiju ćelija",
    "Sekvenciranje svih proteina",
    "Analizu krvnih grupa bez DNK"], 0,
 "Jeffreys je koristio varijabilne minisatelitne/VNTR regione i Southern blot sa specifičnim probama."),
("Zašto su STR markeri postali pogodniji za rutinsku forenzičku analizu od mnogih VNTR lokusa?", [
    "Kraći su i pogodniji za PCR amplifikaciju",
    "Ne sadrže ponovljene sekvence",
    "Postoje samo na Y hromozomu",
    "Ne zahtevaju DNK uzorak"], 0,
 "Kraći STR lokusi mogu se pouzdanije umnožavati PCR-om, uključujući i male ili degradirane uzorke."),
("Koja tvrdnja o Real-time PCR kvantifikaciji iz poglavlja 3 je tačna?", [
    "Može kvantifikovati malu količinu humane DNK i pomoći u proceni degradacije i inhibitora",
    "Detektuje isključivo DNK bakterijskog porekla",
    "Ne koristi fluorescentni signal",
    "Zamenjuje sve korake izolacije DNK"], 0,
 "Udžbenik navodi Real-time PCR kao osetljivu metodu kvantifikacije humane DNK, uz mogućnost procene degradacije i inhibitora."),
]

EXERCISE_QUESTIONS = [
("Šta obuhvata pojam mesta zločina?", [
    "Mesto izvršenja radnje, mesto nastupanja posledice i druga mesta sa relevantnim predmetima i tragovima",
    "Isključivo prostoriju u kojoj je pronađena žrtva",
    "Samo mesto na kome je osumnjičeni uhapšen",
    "Samo laboratoriju u kojoj se analiziraju uzorci"], 0,
 "Mesto zločina može obuhvatiti više lokacija na kojima se nalaze predmeti i tragovi važni za dokazivanje."),
("Koja podela opisuje redosled kategorija mesta zločina?", [
    "Primarno, sekundarno i tercijarno",
    "Vidljivo, nevidljivo i latentno",
    "Fizičko, hemijsko i biološko",
    "Lokalno, regionalno i globalno"], 0,
 "Razlikujemo primarno, sekundarno i tercijarno mesto zločina."),
("Šta je netaknuto mesto zločina?", [
    "Mesto na kome počinilac nije preduzeo radnje prikrivanja ili uništavanja dokaza",
    "Mesto koje je policija već detaljno obradila",
    "Mesto na kome nema bioloških tragova",
    "Mesto koje je namerno prikazano kao nesrećni slučaj"], 0,
 "Netaknuto mesto nije izmenjeno radnjama počinioca radi prikrivanja ili uništavanja dokaza."),
("Šta podrazumeva inscenirano mesto zločina?", [
    "Prikazivanje krivičnog dela kao nesrećnog slučaja",
    "Slučajno pomeranje predmeta tokom fotografisanja",
    "Obeležavanje tragova brojevima",
    "Pakovanje dokaza u laboratoriji"], 0,
 "Inscenirano mesto je vrsta izmenjenog mesta na kome se događaj prikazuje drugačije, npr. kao nesrećni slučaj."),
("Šta je trag u forenzičkom smislu?", [
    "Materijalna promena nastala izvršenjem krivičnog dela koja nosi informacije o poreklu ili uzroku",
    "Isključivo iskaz svedoka",
    "Svaki predmet pronađen u laboratoriji",
    "Samo DNK profil osumnjičenog"], 0,
 "Trag je materijalna promena koja može pomoći u otkrivanju porekla ili identifikaciji uzroka."),
("Kako se naziva nauka o tragovima?", [
    "Traseologija", "Serologija", "Daktiloskopija", "Entomologija"], 0,
 "Traseologija je nauka o tragovima."),
("Koja podela tragova se odnosi na njihovu veličinu?", [
    "Makrotragovi i mikrotragovi",
    "Reljefni i površinski",
    "Ljudski i biljni",
    "Fizički i hemijski"], 0,
 "Prema veličini, tragovi se dele na makro- i mikrotragove."),
("Koja podela se odnosi na izgled traga?", [
    "Reljefni i površinski",
    "Primarni i sekundarni",
    "Ljudski i životinjski",
    "Hemijski i biološki"], 0,
 "Prema izgledu, tragovi mogu biti reljefni ili površinski."),
("Koji je osnovni cilj obezbeđenja lica mesta?", [
    "Očuvanje mesta zločina i tragova što je više moguće neizmenjenim do obrade",
    "Što brže uklanjanje svih predmeta",
    "Dozvoljavanje slobodnog kretanja prisutnih",
    "Odmah uzorkovati svaki predmet bez dokumentovanja"], 0,
 "Obezbeđenje sprečava promenu ili gubitak tragova pre njihove obrade."),
("Navesti definiciju uviđaja.", [
    "Hitna istražna radnja kada je neposredno opažanje potrebno za utvrđivanje ili razjašnjenje važne činjenice",
    "Rutinska laboratorijska analiza DNK",
    "Sudsko saslušanje osumnjičenog",
    "Obavezna radnja koja se sprovodi na svakom mestu događaja"], 0,
 "Uviđaj je hitna istražna radnja; on nije obavezan i zavisi od odluke organa koji vodi postupak."),
("Koja faza obrade lica mesta uključuje prikupljanje informacija razgovorom sa svedocima?", [
    "Informativna/verbalna faza",
    "Statička faza",
    "Dinamička faza",
    "Laboratorijska faza"], 0,
 "Informativna ili verbalna faza obuhvata prikupljanje informacija komunikacijom sa svedocima."),
("Šta je karakteristično za statičku fazu?", [
    "Pregled i dokumentovanje mesta bez dodirivanja i pomeranja predmeta",
    "Odmah pakovanje svih tragova",
    "Uništavanje nevažnih predmeta",
    "Izvođenje DNK amplifikacije na licu mesta"], 0,
 "U statičkoj fazi mesto se posmatra, tragovi identifikuju i dokumentuju bez pomeranja predmeta."),
("Šta se obavlja u dinamičkoj fazi?", [
    "Analiza, fiksiranje, osiguranje i bezbedno pakovanje tragova",
    "Samo razgovor sa svedocima",
    "Samo pregled mesta bez dodirivanja",
    "Isključivo izrada početne skice"], 0,
 "Dinamička faza uključuje obradu i bezbedno prikupljanje materijalnih dokaza."),
("Koji skup aktivnosti pripada kriminalističko-forenzičkoj obradi mesta događaja?", [
    "Intervju, fotodokumentacija, skica, pronalazak i fiksiranje tragova, zapisnici",
    "Samo uzimanje izjava",
    "Samo fotografisanje osumnjičenog",
    "Isključivo DNK sekvenciranje"], 0,
 "Aktivnosti: intervju, fotografisanje, skiciranje, pronalaženje/fiksiranje tragova i dokumentovanje."),
("Koja je svrha skice mesta zločina?", [
    "Da prikaže izgled lica mesta i stvarni položaj žrtve ili dokaza",
    "Da zameni sve fotografije i zapisnike",
    "Da prikaže genetički profil osumnjičenog",
    "Da utvrdi vreme nastanka svake povrede"], 0,
 "Skica prikazuje prostorni raspored i položaj žrtve ili dokaza."),
("Šta je fizički dokaz?", [
    "Svaki predmet koji može povezati žrtvu ili osumnjičenog sa mestom zločina",
    "Samo predmet koji sadrži vidljivu krv",
    "Isključivo DNK profil",
    "Samo iskaz svedoka"], 0,
 "Fizički dokaz može biti predmet koji povezuje učesnike sa mestom zločina."),
("Koja od navedenih grupa predstavlja biološke dokaze?", [
    "Telesne tečnosti i tkiva",
    "Polomljeno staklo i rasuti prah",
    "Otisci cipela i guma",
    "Alati i ključevi"], 0,
 "Razlikujemo dokaze u tragovima, biološke dokaze i uporedne dokaze."),
("Koji biološki materijal je svrstan u I grupu prema potencijalu DNK?", [
    "Sperma i tkiva",
    "Krv (leukociti)",
    "Pljuvačka i sekret iz nosa",
    "Epitelne ćelije kože"], 0,
 "I grupa su sperma i tkiva; II krv; III pljuvačka i sekret iz nosa; IV epitelne ćelije kože."),
("Koje metode se koriste za otkrivanje bioloških tragova?", [
    "Vizuelni pregled, alternativni izvori svetlosti i hemijski reagensi",
    "Samo PCR",
    "Samo rendgensko snimanje",
    "Isključivo mikroskopija elektronskim mikroskopom"], 0,
 "Metode: vizuelni pregled, alternativni izvori svetlosti i hemijski reagensi."),
("Zašto je važno ograničiti broj ljudi na mestu zločina?", [
    "Da bi se smanjila mogućnost kontaminacije tragova",
    "Da bi se povećao broj mogućih tragova",
    "Da bi se ubrzalo sušenje bioloških uzoraka",
    "Da bi se izbegla potreba za dokumentovanjem"], 0,
 "Rizik kontaminacije mesta zločina raste kada broj prisutnih nije ograničen."),
]

LECTURE2_SUMMARY = '\n### 1. Struktura ljudskog genoma\nLjudski genom obuhvata jedarnu DNK (oko 3,2 Gb) i mitohondrijsku DNK (oko 16,5 kb). Podela jedarne DNK na gensku i vangensku(ekstragensku) DNK, kao i na kodirajuće/regulatorne regione, nekodirajuće regione, tandemske i rasute ponovke.\n\n### 2. Satelitska DNK\nNaziv potiče od eksperimenata centrifugiranja DNK u gustinskom gradijentu, kada su uočeni posebni „satelitski“ pojasevi. Satelitska DNK je veoma repetitivna i nalazi se pretežno u heterohromatinu oko centromera i telomera. Učestvuje u organizaciji genoma i održavanju strukture hromozoma.\n\n### 3. Genetička sličnost i polimorfizmi\nLjudi dele oko 99,9% genoma, dok približno 0,1% varijacija doprinosi razlikama među pojedincima. Monomorfni lokusi nemaju uočljivu varijaciju u posmatranoj populaciji, dok se polimorfni lokusi razlikuju među osobama. Polimorfizmi su osnova DNK profilisanja.\n\n### 4. Markeri u forenzičkoj genetici\nForenzičko profilisanje poredi odabrane genetičke markere, a ne čitave genome. Pogodni lokusi su visoko polimorfni, lako i ekonomično se karakterišu, daju profile koji se mogu interpretirati i porediti, imaju nisku mutacionu stopu i nisu pod značajnim selektivnim pritiskom.\n\n### 5. VNTR, STR i SNP\n- **VNTR/minisateliti:** ponavljajuće jedinice od približno 6–100 bp; aleli mogu biti veoma dugi, pa analiza zahteva veću količinu očuvane DNK i interpretacija može biti složena.\n- **STR/mikrosateliti:** kratki tandemски ponovci; motivi su najčešće 1–6 bp, a ukupne dužine alela uglavnom 20–300 bp. Kratki fragmenti pogodni su za PCR i rutinsko forenzičko profilisanje.\n- **SNP:** varijacija pojedinačne baze, najčešće sa dva alela. Pojedinačni SNP je manje polimorfan od STR-a, ali su SNP-ovi brojni u genomu.\n\n### 6. Izolacija i kvantifikacija DNK\nIzolacija obuhvata lizu ćelija, denaturaciju proteina i separaciju DNK od proteina i drugih ćelijskih komponenti. Hemijski postupci koriste deterdžente (SDS, Triton X-100, NP-40), haotropne agense i EDTA; mogu se primeniti i mehaničke metode kao što su sonikacija i bead-beating.\n\nPre daljih analiza procenjuju se količina, kvalitet i stepen degradacije DNK. UV spektrofotometrija meri apsorpciju na 260 nm, dok se odnos OD260/OD280 koristi kao pokazatelj čistoće. Gel-elektroforeza omogućava vizuelizaciju i semi-kvantifikaciju. Fluorimetrija koristi specifične boje/kitove za kvantifikaciju, a PCR omogućava umnožavanje ciljnih STR fragmenata iz malih količina DNK.\n'

LECTURE2_QUESTIONS = [
    ("Koliki deo ukupne ljudske DNK čini kodirajuća DNK?", [
        "Oko 1,5%", "Oko 10%", "Oko 25%", "Oko 75%"], 0,
     "Kodirajući i regulatorni regioni čine približno 1,5% ukupne DNK."),
    ("Šta je alternativni splajsing?", [
        "Proces kojim se iz iste pre-mRNK mogu formirati različite zrele mRNK",
        "Umnožavanje DNK pomoću PCR-a",
        "Razdvajanje DNK fragmenata elektroforezom",
        "Uklanjanje introna iz genoma bez transkripcije"], 0,
     "Alternativni splajsing omogućava nastanak različitih transkripata iz istog gena i doprinosi većem broju proteinskih varijanti."),
    ("Kolika je približna veličina mitohondrijske DNK čoveka?", [
        "16,5 kb", "3,2 Gb", "300 bp", "1,5 Mb"], 0,
     "Mitohondrijski genom čoveka ima približno 16,5 hiljada baznih parova."),
    ("Zašto je satelitska DNK dobila taj naziv?", [
        "Zato što tokom centrifugiranja u gradijentu gustine može formirati odvojene pojaseve",
        "Zato što se nalazi isključivo u mitohondrijama",
        "Zato što kodira proteine neophodne za kretanje ćelije",
        "Zato što se nalazi samo na polnim hromozomima"], 0,
     "Razlike u baznom sastavu mogu dovesti do izdvajanja satelitskih pojaseva od glavnog DNK pojasa."),
    ("Gde se satelitska DNK pretežno nalazi?", [
        "U heterohromatinu oko centromera i telomera",
        "Isključivo u egzonima",
        "U ribozomima",
        "Samo u mitohondrijskom matriksu"], 0,
     "Satelitska DNK je naročito zastupljena u heterohromatinskim regionima oko centromera i telomera."),
    ("Kolika je približna genetička razlika između većine ljudi?", [
        "Oko 0,1% DNK", "Oko 5% DNK", "Oko 10% DNK", "Oko 25% DNK"], 0,
     "Ljudi dele približno 99,9% sekvence genoma, dok oko 0,1% varijacija doprinosi razlikama među pojedincima."),
    ("Koja je glavna uloga polimorfnih lokusa u forenzičkoj genetici?", [
        "Omogućavaju razlikovanje osoba na osnovu varijacija u DNK",
        "Omogućavaju određivanje krvnog pritiska",
        "Određuju starost osobe sa preciznošću od jedne godine",
        "Služe isključivo za određivanje pola"], 0,
     "Polimorfni lokusi imaju različite alele među osobama i zato su informativni za DNK profilisanje."),
    ("Kako se naziva lokus čija je sekvenca ista među osobama u određenoj populaciji?", [
        "Monomorfni lokus", "Polimorfni lokus", "STR lokus", "SNP lokus"], 0,
     "Monomorfni lokus nema uočljivu varijaciju sekvence u posmatranoj populaciji."),
    ("Koja osobina je poželjna kod lokusa koji se koriste u forenzičkoj genetici?", [
        "Visoka polimorfnost i niska mutaciona stopa",
        "Visoka mutaciona stopa i jaka selekcija",
        "Nemogućnost poređenja rezultata između laboratorija",
        "Isključivo prisustvo u kodirajućim regionima"], 0,
     "Forenzički markeri treba da budu informativni, stabilni i jednostavni za karakterizaciju i poređenje."),
    ("Koja je osnovna razlika između VNTR i STR lokusa?", [
        "Razlikuju se po dužini osnovne ponavljajuće jedinice",
        "VNTR se nalaze samo u mitohondrijama, a STR samo u jedru",
        "STR nemaju ponovljene sekvence",
        "VNTR predstavljaju promene jedne baze"], 0,
     "VNTR imaju motive približno 6–100 bp, dok su STR motivi uglavnom 1–6 bp."),
    ("Koja je tipična dužina ponavljajućeg motiva kod VNTR lokusa?", [
        "6–100 bp", "1–6 bp", "100–500 bp", "Tačno 1 bp"], 0,
     "Minisatelitski VNTR motivi imaju približno 6 do 100 baznih parova."),
    ("Zašto se VNTR lokusi danas ređe koriste u rutinskoj forenzici?", [
        "Često zahtevaju veću količinu nedegradovane DNK, a interpretacija može biti složena",
        "Nemaju varijabilnost među osobama",
        "Ne mogu se analizirati restrikcionim enzimima",
        "Nalaze se samo kod bakterija"], 0,
     "Dugački VNTR fragmenti teže se analiziraju u malim ili degradiranim uzorcima."),
    ("Koja je osobina STR lokusa posebno korisna za forenzičko profilisanje?", [
        "Kratki su i mogu se umnožavati PCR metodom",
        "Uvek imaju samo jedan alel",
        "Ne postoje na autozomima",
        "Ne mogu se analizirati u mešanim uzorcima"], 0,
     "Kratka dužina STR alela omogućava PCR amplifikaciju i analizu male količine DNK."),
    ("Koji tip STR motiva je čest u forenzičkim analizama?", [
        "Tetranukleotidni ponovci", "Ponovci od 50 nukleotida", "Jedinični proteinski motivi", "Motivi od 1000 bp"], 0,
     "Mnogi STR lokusi koji se koriste u forenzici imaju tetranukleotidne motive."),
    ("Šta predstavlja SNP?", [
        "Varijaciju u jednom nukleotidu DNK sekvence",
        "Promenu broja čitavih hromozoma",
        "Ponavljanje motiva od 100 baznih parova",
        "Razliku u dužini proteinskog lanca"], 0,
     "SNP je polimorfizam jednog nukleotida; najčešće postoje dva alela na datom mestu."),
    ("Zašto SNP markeri pojedinačno imaju manju diskriminatornu moć od STR lokusa?", [
        "Najčešće imaju samo dva alela",
        "U genomu se javljaju samo jednom",
        "Ne mogu se nasleđivati",
        "Uvek su pod jakim selektivnim pritiskom"], 0,
     "Bialelna priroda većine SNP-ova znači da je pojedinačni lokus manje polimorfan od STR lokusa."),
    ("Koji uslovi pogoduju dugotrajnom očuvanju DNK?", [
        "Niska temperatura, suvoća i odsustvo svetlosti",
        "Visoka temperatura i velika vlažnost",
        "Direktna sunčeva svetlost",
        "Čuvanje vlažnog materijala u zatvorenoj plastici na sobnoj temperaturi"], 0,
     "Hladni, suvi i tamni uslovi usporavaju procese degradacije DNK."),
    ("Koji je osnovni cilj hemijske lize tokom izolacije DNK?", [
        "Narušavanje ćelijskih membrana i oslobađanje ćelijskog sadržaja",
        "Umnožavanje STR lokusa",
        "Razdvajanje alela po veličini",
        "Određivanje koncentracije DNK UV svetlošću"], 0,
     "Hemijska liza koristi reagense koji rastvaraju membrane i oslobađaju DNK."),
    ("Koja je uloga EDTA tokom izolacije DNK?", [
        "Vezuje dvovalentne jone i inhibira DNK-aze",
        "Seče DNK na specifičnim sekvencama",
        "Fluorescentno obeležava STR alele",
        "Umnožava ciljnu DNK sekvencu"], 0,
     "EDTA helira jone poput Mg2+, koji su potrebni mnogim DNK-azama."),
    ("Šta se može proceniti odnosom apsorbancija A260/A280?", [
        "Čistoća DNK u odnosu na proteinsku kontaminaciju",
        "Broj STR alela",
        "Dužina svakog hromozoma",
        "Broj ćelija u uzorku"], 0,
     "Za relativno čistu DNK očekuje se odnos A260/A280 približno 1,8.")
]

EXERCISE2_SUMMARY = '\n### 1. Opšta načela postupanja sa biološkim tragovima\nTragovi se uočavaju, fotografišu, evidentiraju, prikupljaju/izuzimaju i pakuju za dalju analizu. Važni su količina, čistoća i brzo dostavljanje uzorka. Svaki trag se zasebno obeležava i pakuje; koristi se sterilan pribor, jednokratne rukavice i zaštitna oprema, uz minimalnu manipulaciju i sprečavanje unakrsne kontaminacije.\n\n### 2. Prikupljanje i pakovanje\nSa velikih i nepokretnih podloga tragovi se uzorkuju sterilnim brisevima. Vlažne tragove je poželjno osušiti pre uzorkovanja; veoma suvi tragovi mogu se uzorkovati blago navlaženim brisem/filter-papirom ili struganjem. Suvi tragovi se mogu izuzeti struganjem na čist papir, izrezivanjem dela podloge ili izuzimanjem celog predmeta. Odeća sa tragovima pakuje se u papirnu ambalažu. Tečni uzorci se čuvaju u odgovarajućim sterilnim epruvetama.\n\n### 3. Krv\nTragovi krvi mogu biti slivanje, natapanje tkanine, lokve, prskotine, tragovi preneti dodirom i ostaci krvi; indirektni tragovi mogu nastati ispiranjem zakrvavljenih predmeta. Svaki trag se fotografiše, obeležava i pakuje odvojeno. Tečna krv za DNK analizu može se uzeti u epruvete sa EDTA; heparin nije preporučljiv zbog mogućeg inhibitornog uticaja. Za toksikološke analize koristi se natrijum-fluorid. Luminol i preliminarne test-trake ukazuju na moguće prisustvo krvi, ali pozitivna preliminarna reakcija sama po sebi ne dokazuje ljudsko poreklo. Potvrdni testovi mogu utvrditi humano poreklo.\n\n### 4. Sperma\nTragovi sperme mogu biti tečni ili sasušeni. Tečni tragovi mogu se prikupiti suvim sterilnim brisem ili pipetom, a bris se suši pre pakovanja. Sasušene mrlje se pakuju sa predmetom ili se izuzima deo podloge. UV svetlost može pomoći u lokalizaciji, a preliminarni testovi mogu detektovati kiselu fosfatazu. Potvrdne metode uključuju detekciju PSA, semenogelina i mikroskopsku identifikaciju spermatozoida.\n\n### 5. Pljuvačka, urin i dlake\nPljuvačka sadrži epitelne ćelije i može se naći na opušcima, žvakama, kovertama, čašama i predmetima za ličnu upotrebu. Preliminarni testovi mogu detektovati aktivnost α-amilaze; DNK analiza se koristi za identifikaciju. Urin se može lokalizovati vizuelno ili UV svetlošću; preliminarni testovi mogu detektovati ureu ili kreatinin. Nepoznate dlake uzimaju se čistom pincetom bez oštećivanja korena i pakuju pojedinačno; referentne dlake uzimaju se sa više regiona vlasišta.\n\n### 6. Čuvanje, degradacija i kontaminacija\nDegradaciju ubrzavaju temperatura, vlaga, sunčeva svetlost, hemikalije i mikroorganizmi. Osušeni biološki materijal se čuva u papirnoj ambalaži, na suvom, hladnom i tamnom mestu. Kontaminacija može nastati u bilo kojoj fazi i mora se sprečavati odgovarajućom zaštitnom opremom, promenom rukavica, sterilnim priborom i zasebnim pakovanjem.\n'

EXERCISE2_QUESTIONS = [
    ("Koji je prvi korak nakon uočavanja biološkog traga na mestu događaja?", [
        "Označavanje, opisivanje i fotodokumentovanje traga",
        "Odmah mešanje sa drugim uzorcima",
        "Pakovanje bez prethodnog pregleda",
        "Pranje površine radi uklanjanja viška materijala"], 0,
     "Trag se najpre fiksira dokumentovanjem, obeležavanjem i fotografisanjem, a zatim prikuplja."),
    ("Kako se uzorkuju tragovi na velikim i nepokretnim površinama?", [
        "Sterilnim brisevima",
        "Isključivo pincetom",
        "Uvek izrezivanjem cele površine",
        "Papirnom maramicom koja se koristi za više tragova"], 0,
     "Sterilni brisevi omogućavaju uzorkovanje tragova sa velikih ili nepokretnih podloga."),
    ("Zašto je poželjno osušiti vlažan biološki trag pre pakovanja?", [
        "Da bi se smanjio uticaj mikroorganizama i degradacija materijala",
        "Da bi se povećao sadržaj vode u uzorku",
        "Da bi se uklonila ljudska DNK",
        "Da bi se sprečilo izdvajanje ćelija"], 0,
     "Vlažnost pogoduje razvoju mikroorganizama koji mogu oštetiti biološki materijal."),
    ("Kako se postupa sa veoma sasušenim tragom koji se uzorkuje brisom?", [
        "Bris se može nakvasiti sterilnim fiziološkim rastvorom ili destilovanom vodom",
        "Trag se natapa običnom vodom iz česme",
        "Površina se pere deterdžentom",
        "Uzorak se zagreva do ključanja"], 0,
     "Blago navlažen sterilni bris može efikasnije prikupiti veoma sasušeni materijal."),
    ("Zašto se koriste odvojene rukavice ili njihova zamena između uzoraka?", [
        "Da bi se sprečio prenos biološkog materijala između tragova",
        "Da bi se ubrzala amplifikacija DNK",
        "Da bi se povećala količina uzorka",
        "Da bi se izbeglo fotografisanje"], 0,
     "Promena rukavica smanjuje rizik od unakrsne kontaminacije."),
    ("Kako se uzorci različitih tragova pakuju?", [
        "Svaki trag u zasebnu, odgovarajuću ambalažu",
        "Svi tragovi zajedno u jednu kesu",
        "Samo u hermetički zatvorenu plastičnu kesu",
        "Bez ambalaže, uz zajedničku oznaku"], 0,
     "Odvojeno pakovanje sprečava međusobni kontakt i kontaminaciju uzoraka."),
    ("Koja ambalaža je pogodna za osušenu odeću sa tragovima krvi?", [
        "Papirna kesa ili papirni džak",
        "Vlažna plastična kesa",
        "Staklena posuda napunjena vodom",
        "Otvorena posuda bez oznake"], 0,
     "Odeća sa osušenim tragovima pakuje se u papirnu ambalažu koja omogućava razmenu vlage."),
    ("Koji antikoagulans se može nalaziti u epruveti za uzorkovanje krvi za DNK analizu?", [
        "EDTA", "Heparin", "Natrijum-fluorid", "Etanol"], 0,
     "EDTA sprečava koagulaciju; heparin se izbegava jer može inhibirati DNK analizu."),
    ("Zašto se heparin ne preporučuje za uzorke krvi namenjene DNK analizi?", [
        "Može inhibirati dalju DNK analizu",
        "Razgrađuje sve eritrocite",
        "Pretvara DNK u RNK",
        "Uklanja leukocite iz uzorka"], 0,
     "Heparin može delovati kao inhibitor u molekularnim analizama."),
    ("Koji dodatak se koristi u epruvetama za krv namenjenu toksikološkoj analizi?", [
        "Natrijum-fluorid", "EDTA u svim slučajevima", "Proteinaza K", "Agaroza"], 0,
     "Za toksikološke analize tečna krv se može uzeti u epruvete sa natrijum-fluoridom."),
    ("Kako se uzorkuje suv trag krvi sa velike, glatke površine?", [
        "Sterilnim brisom navlaženim fiziološkim rastvorom ili destilovanom vodom",
        "Pamučnom krpom korišćenom za više tragova",
        "Direktnim ispiranjem u odvod",
        "Dodavanjem deterdženta i struganjem"], 0,
     "Navlažen sterilni bris omogućava prikupljanje osušenog traga sa površine."),
    ("Koji oblik svetlosnog signala nastaje u reakciji luminola sa tragom krvi?", [
        "Plava hemiluminiscencija",
        "Crvena fluorescencija",
        "Zelena fosforescencija",
        "Žuta apsorpcija"], 0,
     "U prisustvu vodonik-peroksida i hemoglobina luminol daje plavu hemiluminiscenciju."),
    ("Šta pokazuje pozitivan preliminarni test na krv?", [
        "Da je potreban dalji postupak potvrde i ispitivanja porekla traga",
        "Da je trag sigurno ljudska krv",
        "Da je DNK profil već identifikovan",
        "Da trag potiče od određene osobe"], 0,
     "Preliminarna reakcija ukazuje na moguće prisustvo krvi, ali ne utvrđuje ljudsko poreklo niti identitet."),
    ("Koji princip koristi Hemastix test?", [
        "Katalitičku aktivnost hemoglobina u reakciji oksidacije",
        "Detekciju STR alela fluorescentnim bojama",
        "Precipitaciju DNK",
        "Merenje apsorbancije na 260 nm"], 0,
     "Testne trake registruju reakciju povezanu sa katalitičkom aktivnošću hemoglobina."),
    ("Koji test se koristi za potvrdu humanog porekla traga krvi?", [
        "Imunohromatografski test koji prepoznaje humane krvne proteine",
        "Luminol test",
        "Phosphatesmo test",
        "Skrob-jodni test"], 0,
     "Testovi kao što su ABAcard HemaTrace i OBTI koriste imunološko prepoznavanje humanih krvnih proteina."),
    ("Koji enzim se koristi u preliminarnom testiranju tragova sperme?", [
        "Kisela fosfataza", "α-amilaza", "Ureaza", "DNK-polimeraza"], 0,
     "Kisela fosfataza se nalazi u visokoj koncentraciji u spermi i osnova je testa Phosphatesmo."),
    ("Koji nalaz predstavlja potvrdni pristup za identifikaciju sperme?", [
        "Detekcija PSA ili spermatozoida mikroskopskom analizom",
        "Samo plavo obojenje luminolom",
        "Detekcija uree",
        "Merenje apsorbancije na 280 nm"], 0,
     "PSA testiranje i mikroskopska detekcija spermatozoida predstavljaju potvrdne pristupe."),
    ("Koji enzim se koristi u preliminarnom testiranju pljuvačke?", [
        "α-amilaza", "Kisela fosfataza", "Ureaza", "Katalaza"], 0,
     "Pljuvačka sadrži α-amilazu; njena aktivnost može se ispitivati skrob-jodnim testom."),
    ("Zašto je pljuvačka pogodna za DNK analizu?", [
        "Često sadrži epitelne ćelije sa jedarnom DNK",
        "Sadrži isključivo slobodnu mitohondrijsku DNK",
        "Ne sadrži mikroorganizme",
        "Uvek sadrži spermatozoide"], 0,
     "Epitelne ćelije usne duplje predstavljaju izvor humane jedarne DNK."),
    ("Zašto se osušeni biološki tragovi najčešće pakuju u papirnu ambalažu?", [
        "Papir omogućava razmenu vlage i smanjuje rizik od razvoja plesni i buđi",
        "Papir sprečava svaku promenu DNK tokom neograničenog vremena",
        "Papir sterilizuje uzorak",
        "Papir uklanja kontaminaciju koja je već prisutna"], 0,
     "Dobro osušeni tragovi u papirnoj ambalaži imaju manji rizik od zadržavanja vlage i razvoja mikroorganizama.")
]


def prepare_quiz_questions(key, questions):
    """Stabilno nasumično menja redosled pitanja i ponuđenih odgovora."""
    seed_key = f"_quiz_seed_{key}"
    if seed_key not in st.session_state:
        st.session_state[seed_key] = random.SystemRandom().randint(0, 2**32 - 1)
    rng = random.Random(st.session_state[seed_key])
    shuffled_questions = list(questions)
    rng.shuffle(shuffled_questions)

    correct_positions = [0, 1, 2, 3] * (len(shuffled_questions) // 4)
    correct_positions += list(range(len(shuffled_questions) % 4))
    rng.shuffle(correct_positions)

    prepared = []
    for item, correct_position in zip(shuffled_questions, correct_positions):
        question, options, correct_index, explanation = item
        correct_answer = options[correct_index]
        distractors = [option for index, option in enumerate(options) if index != correct_index]
        rng.shuffle(distractors)
        shuffled_options = list(distractors)
        shuffled_options.insert(correct_position, correct_answer)
        prepared.append((question, shuffled_options, correct_position, explanation))
    return prepared


def render_quiz(key, questions):
    questions = prepare_quiz_questions(key, questions)
    st.subheader("Kviz")
    st.caption("Izaberite po jedan odgovor za svako pitanje, a zatim kliknite na „Proveri odgovore“.")
    with st.form(f"form_{key}"):
        answers = []
        for i, (q, opts, correct, explanation) in enumerate(questions, 1):
            st.markdown(f"**{i}. {q}**")
            answer = st.radio(
                "Odaberite odgovor:", opts, index=None,
                key=f"{key}_q{i}", label_visibility="collapsed",
                format_func=lambda option, choices=opts: f"{chr(65 + choices.index(option))}. {option}",
            )
            answers.append(answer)
            if i != len(questions):
                st.divider()
        submitted = st.form_submit_button("Proveri odgovore", type="primary", use_container_width=True)

    if submitted:
        score = sum(answer == item[1][item[2]] for answer, item in zip(answers, questions))
        st.markdown("### Rezultat")
        st.metric("Tačni odgovori", f"{score} / {len(questions)}", f"{score/len(questions)*100:.0f}%")
        if score == len(questions):
            st.success("Odlično! Svi odgovori su tačni.")
        elif score >= 15:
            st.success("Veoma dobro! Ponovite samo pitanja na koja niste tačno odgovorili.")
        elif score >= 10:
            st.info("Dobar početak. Pregledajte objašnjenja i ponovite sažetak.")
        else:
            st.warning("Preporuka: prvo ponovite sažetak lekcije, pa pokušajte ponovo.")

        with st.expander("Prikaži tačne odgovore i objašnjenja", expanded=True):
            for i, (answer, item) in enumerate(zip(answers, questions), 1):
                q, opts, correct, explanation = item
                correct_answer = opts[correct]
                correct_label = chr(65 + correct)
                is_correct = answer == correct_answer
                st.markdown(f"**{i}. {'Tačno' if is_correct else 'Netačno'}**")
                st.write(q)
                st.write(f"Tačan odgovor: **{correct_label}. {correct_answer}**")
                if answer is None:
                    st.caption("Nije izabran odgovor.")
                elif not is_correct:
                    selected_label = chr(65 + opts.index(answer))
                    st.caption(f"Vaš odgovor: {selected_label}. {answer}")
                st.caption(explanation)
                if i != len(questions):
                    st.divider()

tab_predavanja, tab_vezbe = st.tabs(["📘 Predavanja", "🔬 Vežbe"])

with tab_predavanja:
    predavanje1, predavanje2 = st.tabs(["Predavanje 1 — Uvod", "Predavanje 2 — DNK analiza"])
    with predavanje1:
        st.header("Predavanje 1: Uvod u forenzičku genetiku")
        with st.expander("Sažetak lekcije", expanded=True):
            st.markdown(LECTURE_SUMMARY)
        render_quiz("lecture1", LECTURE_QUESTIONS)
    with predavanje2:
        st.header("Predavanje 2: Forenzička genetika — DNK analiza bioloških tragova")
        with st.expander("Sažetak lekcije", expanded=True):
            st.markdown(LECTURE2_SUMMARY)
        render_quiz("lecture2", LECTURE2_QUESTIONS)

with tab_vezbe:
    vezbe1, vezbe2 = st.tabs(["Vežba 1 — Mesto zločina", "Vežba 2 — Uzorkovanje"])
    with vezbe1:
        st.header("Vežba 1: Mesto zločina i tragovi sa lica mesta")
        with st.expander("Sažetak lekcije", expanded=True):
            st.markdown(EXERCISE_SUMMARY)
        render_quiz("exercise1", EXERCISE_QUESTIONS)
    with vezbe2:
        st.header("Vežba 2: Uzorkovanje i testiranje bioloških tragova")
        with st.expander("Sažetak lekcije", expanded=True):
            st.markdown(EXERCISE2_SUMMARY)
        render_quiz("exercise2", EXERCISE2_QUESTIONS)

st.divider()
st.caption(
    "Materijal je namenjen za samostalno obnavljanje gradiva. Pitanja su sastavljena prema dostavljenim "
    "nastavnim materijalima."
)
