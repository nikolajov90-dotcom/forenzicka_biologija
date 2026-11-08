import streamlit as st

st.set_page_config(
    page_title="Forenzička biologija | Obnavljanje gradiva",
    page_icon="🧬",
    layout="wide",
)

st.title("🧬 Forenzička biologija 2026/2027")
st.caption("Interaktivno obnavljanje gradiva")
st.markdown(
    """
    Izaberite karticu za **predavanja** ili **vežbe**. U svakoj lekciji
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
("Šta opisuje centralna dogma molekularne biologije u okviru predavanja?", [
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
("Šta obuhvata pojam mesta zločina prema materijalu sa vežbi?", [
    "Mesto izvršenja radnje, mesto nastupanja posledice i druga mesta sa relevantnim predmetima i tragovima",
    "Isključivo prostoriju u kojoj je pronađena žrtva",
    "Samo mesto na kome je osumnjičeni uhapšen",
    "Samo laboratoriju u kojoj se analiziraju uzorci"], 0,
 "Mesto zločina može obuhvatiti više lokacija na kojima se nalaze predmeti i tragovi važni za dokazivanje."),
("Koji redosled kategorija mesta zločina je naveden u prezentaciji?", [
    "Primarno, sekundarno i tercijarno",
    "Vidljivo, nevidljivo i latentno",
    "Fizičko, hemijsko i biološko",
    "Lokalno, regionalno i globalno"], 0,
 "Prezentacija razlikuje primarno, sekundarno i tercijarno mesto zločina."),
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
("Kako je u prezentaciji definisan uviđaj?", [
    "Hitna istražna radnja kada je neposredno opažanje potrebno za utvrđivanje ili razjašnjenje važne činjenice",
    "Rutinska laboratorijska analiza DNK",
    "Sudsko saslušanje osumnjičenog",
    "Obavezna radnja koja se sprovodi na svakom mestu događaja"], 0,
 "Uviđaj je hitna istražna radnja; prezentacija navodi da nije obavezan i da zavisi od odluke organa koji vodi postupak."),
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
 "Prezentacija navodi intervju, fotografije, skicu, pronalaženje/fiksiranje tragova i dokumentaciju."),
("Koja je svrha skice mesta zločina?", [
    "Da prikaže izgled lica mesta i stvarni položaj žrtve ili dokaza",
    "Da zameni sve fotografije i zapisnike",
    "Da prikaže genetički profil osumnjičenog",
    "Da utvrdi vreme nastanka svake povrede"], 0,
 "Skica prikazuje prostorni raspored i položaj žrtve ili dokaza."),
("Šta je fizički dokaz prema prezentaciji?", [
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
 "Prezentacija razlikuje dokaze u tragovima, biološke dokaze i uporedne dokaze."),
("Koji biološki materijal je u prezentaciji svrstan u I grupu prema potencijalu DNK?", [
    "Sperma i tkiva",
    "Krv (leukociti)",
    "Pljuvačka i sekret iz nosa",
    "Epitelne ćelije kože"], 0,
 "Prema podeli sa vežbi: I grupa su sperma i tkiva; II krv; III pljuvačka i sekret iz nosa; IV epitelne ćelije kože."),
("Koje metode se koriste za otkrivanje bioloških tragova?", [
    "Vizuelni pregled, alternativni izvori svetlosti i hemijski reagensi",
    "Samo PCR",
    "Samo rendgensko snimanje",
    "Isključivo mikroskopija elektronskim mikroskopom"], 0,
 "Prezentacija navodi vizuelni pregled, alternativne izvore svetlosti i hemijske reagense."),
("Zašto je važno ograničiti broj ljudi na mestu zločina?", [
    "Da bi se smanjila mogućnost kontaminacije tragova",
    "Da bi se povećao broj mogućih tragova",
    "Da bi se ubrzalo sušenje bioloških uzoraka",
    "Da bi se izbegla potreba za dokumentovanjem"], 0,
 "Prema prezentaciji, rizik kontaminacije mesta zločina raste kada broj prisutnih nije ograničen."),
]

def render_quiz(key, questions):
    st.subheader("Kviz — 20 pitanja")
    st.caption("Izaberite po jedan odgovor za svako pitanje, a zatim kliknite na „Proveri odgovore“.")
    with st.form(f"form_{key}"):
        answers = []
        for i, (q, opts, correct, explanation) in enumerate(questions, 1):
            st.markdown(f"**{i}. {q}**")
            answer = st.radio(
                "Odaberite odgovor:",
                opts,
                index=None,
                key=f"{key}_q{i}",
                label_visibility="collapsed",
            )
            answers.append(answer)
            if i != len(questions):
                st.divider()
        submitted = st.form_submit_button("Proveri odgovore", type="primary", use_container_width=True)

    if submitted:
        score = 0
        for answer, item in zip(answers, questions):
            if answer == item[1][item[2]]:
                score += 1
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
                is_correct = answer == correct_answer
                st.markdown(f"**{i}. {'Tačno' if is_correct else 'Netačno'}**")
                st.write(q)
                st.write(f"Tačan odgovor: **{correct_answer}**")
                if answer is None:
                    st.caption("Nije izabran odgovor.")
                elif not is_correct:
                    st.caption(f"Vaš odgovor: {answer}")
                st.caption(explanation)
                if i != len(questions):
                    st.divider()

tab1, tab2 = st.tabs(["📘 Prvo predavanje — Forenzička genetika", "🔬 Prve vežbe — Mesto zločina i tragovi"])

with tab1:
    st.header("Prvo predavanje: Uvod u forenzičku genetiku")
    with st.expander("Sažetak lekcije", expanded=True):
        st.markdown(LECTURE_SUMMARY)
    render_quiz("lecture", LECTURE_QUESTIONS)

with tab2:
    st.header("Prve vežbe: Mesto zločina i tragovi sa lica mesta")
    with st.expander("Sažetak lekcije", expanded=True):
        st.markdown(EXERCISE_SUMMARY)
    render_quiz("exercise", EXERCISE_QUESTIONS)

st.divider()
st.caption(
    "Materijal je namenjen za samostalno obnavljanje gradiva. Pitanja su sastavljena prema dostavljenim "
    "nastavnim materijalima."
)
