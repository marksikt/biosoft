# Banca de cunoștințe — Metabolism, Îmbătrânire și Sistemul Neuro-Glio-Vascular

**Sursă:** Shichkova et al. (2025). *Breakdown and repair of metabolism in the aging brain.*  
Frontiers in Science, 3:1441297. doi: 10.3389/fsci.2025.1441297  
**Blue Brain Project, EPFL Geneva**  
**Acces model open-source:** https://github.com/BlueBrain/metabolism-in-aging  
**Extras pentru:** modelare organism uman — nivel conceptual  

---

## 1. Principii arhitecturale de modelare

### 1.1 Sistemul NGV ca unitate de bază
Modelul tratează creierul ca un sistem de unități **neuro-glio-vasculare (NGV)**:
- 1 neuron + 1 astrocit + matricea extracelulară asociată + capilarul aferent = 1 unitate NGV
- Aceasta este granularitatea minimă relevantă pentru modelarea energetică
- Fiecare unitate este semi-autonomă dar puternic cuplată cu vecinii

### 1.2 Cele trei subsisteme cuplate
Orice model realist al creierului trebuie să integreze simultan:
1. **Metabolism molecular** — enzime, transportori, metaboliți
2. **Electrofizologie neuronală** — potențiale de acțiune, curenți ionici
3. **Flux sanguin** — aport de nutrienți, oxigen, evacuare deșeuri

Cuplarea dintre ele nu este opțională — modificarea unuia le perturbă pe celelalte. Modelele care izolează un subsistem pierd comportamente emergente esențiale.

### 1.3 Strategie de construcție bottom-up
Autorii recomandă construcția iterativă:
- Pornește de la reacțiile individuale bine constrânse (hexokinaza, lanțul de transport electroni)
- Combină treptat în căi metabolice
- Conectează căile în celule (neuron, astrocit separat)
- Conectează celulele între ele
- Conectează metabolismul cu electrofizologia și vasculatura

**Principiu cheie:** Optimizează doar pentru starea de repaus (steady state), nu pentru a reproduce dinamici de serii de timp — datele de serii de timp sunt rare și contradictorii.

### 1.4 Scara modelului din acest articol
- **183 procese** modelate (95 reacții enzimatice, 19 transporturi transmembranare, 69 alte procese)
- **151 ecuații diferențiale** pentru concentrații moleculare variabile
- **16.800 căi de interacțiune** enzimă/transportor–metabolit
- **Compartimente:** citosolul neuronal, citosolul astrocitar, matricea mitocondrială, spațiul intermembranar mitocondrial, interstițiu, lamina bazală, endoteliu, capilar, arteră

---

## 2. Metabolism energetic — principii conceptuale

### 2.1 ATP nu este singurul indicator relevant
Modelul arată că **AEC (Adenylate Energy Charge)** este mai informativ decât [ATP] singur:

```
AEC = (ATP + 0.5 × ADP) / (ATP + ADP + AMP)
```

AEC integrează întregul pool adenilat și reflectă mai fidel capacitatea energetică celulară. Creierul tânăr menține AEC mai ridicat decât cel îmbătrânit.

### 2.2 Producție vs. consum — nu sunt echivalente
Îmbătrânirea reduce **atât producția cât și consumul de ATP**. Concluzia contraintuitivă: ATP supply nu este factorul limitant al disfuncției. Consumul scade pentru că pompa principală (Na⁺/K⁺-ATPase) este downregulată.

Implicație pentru modelare: **nu confunda deficiența energetică cu deficiența de funcție**. Un sistem poate avea ATP suficient și totuși să nu funcționeze corect dacă mecanismele de utilizare sunt compromise.

### 2.3 Compartimentare mitocondrială vs. citosol
Producția de ATP este diferită în cele două compartimente și trebuie modelată separat:
- **Neuroni:** 84% din ATP din mitocondrii, 16% din citosolul
- **Astrocite:** 70% din mitocondrii, 30% din citosolul

Îmbătrânirea afectează diferit cele două compartimente și cele două tipuri celulare.

### 2.4 NAD⁺/NADH — hub redox central
Pool-ul total NAD (oxidat + redus) scade cu îmbătrânirea. Raportul NAD⁺/NADH reglează rețeaua metabolică în ansamblu, inclusiv:
- Glicoliza
- Ciclul TCA
- Lanțul de transport electroni
- Activitatea LDH (lactat dehidrogenaza)

**Shuttlul NADH citosol–mitocondrie** (malat-aspartat + glicerol-fosfat) este un punct de control critic. Reducerea sa cu îmbătrânirea perturbă echilibrul redox global.

### 2.5 Corpii cetonici ca combustibil alternativ
β-hidroxibutiratul (β-HB) este un substrat energetic alternativ glucozei, preluat atât de neuroni cât și de astrocite. Nivelul său scade cu îmbătrânirea. Creșterea sa (prin dietă cetogenică sau restricție calorică) este una dintre intervențiile eficiente identificate de model.

### 2.6 Calea pentozelor fosfat (PPP) și stresul oxidativ
PPP produce NADPH, esențial pentru regenerarea glutationului (GSH) — principalul antioxidant celular. Modelul include:
- Glutationa peroxidaza (GPX)
- GSSG reductaza
- NOX (NADPH oxidaza)

Îmbătrânirea perturbă balanța redox și prin această cale.

---

## 3. Sistemul nervos — electrofizologie și cuplare metabolică

### 3.1 Pompa Na⁺/K⁺-ATPase — elementul critic
**Descoperire centrală a articolului:** Cauza principală a degradării potențialelor de acțiune în îmbătrânire nu este lipsa ATP, ci **reducerea expresiei pompei Na⁺/K⁺-ATPase**.

- Pompa consumă ~31% din energia totală a unității NGV
- Scăderea expresiei ei modifică forma și amplitudinea potențialului de acțiune
- Restaurarea expresiei ei la nivelul tânăr restabilește firing-ul neuronal, chiar dacă restul metabolismului rămâne îmbătrânit

Implicație: într-un model al creierului, pompa ionică este **mai importantă decât producția de ATP** pentru funcția neuronală.

### 3.2 Model electrofizologic — tip Hodgkin-Huxley extins
Autorii folosesc un model HH extins (nu simplificat):
- Curenți modelați: Na⁺, K⁺, K⁺ lent (după hiperpolarizare), curent de scurgere
- AHP (afterhyperpolarization) — reglat de curentul K⁺ Ca²⁺-dependent
- Cuplare explicită cu metabolismul prin Na⁺/K⁺-ATPase

### 3.3 Caracteristici ale potențialului de acțiune afectate de îmbătrânire
- Amplitudine redusă
- Rată de creștere (rise rate) redusă
- Rată de scădere (fall rate) modificată
- Lărgime (half-width) crescută
- AHP modificat

### 3.4 Ciclul glutamat-glutamină
Un circuit metabolic esențial între neuroni și astrocite:
- Glutamatul eliberat sinaptic este recaptat de astrocite
- Astrocitele îl convertesc în glutamină (prin glutamina sintetaza)
- Glutamina este returnată neuronilor
- Acest ciclu consumă ATP astrocitar și este perturbat de îmbătrânire (eliberarea sinaptică de glutamat scade)

---

## 4. Sistemul vascular și aportul de nutrienți

### 4.1 Glucoza — compartimentare detaliată
Transportul glucozei trebuie modelat prin toate compartimentele, nu direct din sânge în celulă:

```
Arteră → Capilar → Endoteliu → Lamina bazală → Interstițiu → Astrocit / Neuron
```

La fiecare interfață există transportori specifici (GLUT1, GLUT3) cu cinematică proprie (trans-accelerare, asimetrie). Simplificarea acestui lanț produce erori semnificative.

### 4.2 Flux hexokinazei ca ancoră metabolică
CMR (cerebral metabolic rate) de glucoză este bine măsurat experimental — aceasta constrânge parametrul Vmax al hexokinazei. Este punctul de plecare recomandat pentru orice model de metabolism cerebral.

La repaus: fluxul hexokinazei este egal între neuron și astrocit (~50/50).  
La activare: raportul se deplasează spre astrocit.

### 4.3 Activarea fluxului sanguin
Modelul folosește o funcție simplă dependentă de debutul și durata stimulului (nu mecanistic). Limitele actuale ale modelului:
- Nu include reglarea mecanistică a fluxului sanguin prin activare neuronală
- Nu modelează variațiile de disponibilitate a oxigenului cu îmbătrânirea

### 4.4 Semnalul BOLD și OGI — validare de nivel înalt
Modelul reproduce:
- Semnalul BOLD (blood-oxygen-level-dependent) — folosit în fMRI
- OGI (oxygen-glucose index): 4.5–5.0 (literatura: 4.0–5.5)

Acestea sunt benchmarkuri standard pentru modele NGV.

---

## 5. Îmbătrânire și neurodegenerare — principii conceptuale

### 5.1 Îmbătrânirea ca perturbație multi-nivel
Modelul implementează îmbătrânirea prin modificări la mai multe niveluri simultan:
1. **Transcriptom:** fold changes RNA pentru fiecare enzimă și transportor (date Tabula Muris Senis — mouse, single-cell)
2. **Nutrienți sanguini:** glucoză ↑, lactat ↑, β-HB ↓
3. **Pool NAD total:** ↓
4. **Shuttlul NADH citosol-mitocondrie:** ↓
5. **Eliberarea sinaptică de glutamat:** ↓

**Atenție metodologică:** datele RNA sunt folosite ca proxy pentru concentrațiile proteice — corelația RNA-proteină este imperfectă. Datele proteomice celulă-specifice pentru vârstă sunt încă insuficiente.

### 5.2 Adaptabilitate metabolică — metrica de fragilitate
Autorii definesc o metrică nouă, **metabolic adaptability**:

```
adaptability(metabolit, enzimă) = 
  sensitivity_stimulat - sensitivity_repaus
  ————————————————————————————————————————
           sensitivity_repaus
```

unde sensitivity = variația relativă a concentrației metabolitului la perturbarea ±20% a parametrului cinetic al enzimei.

- Valoare mare = metabolitul răspunde bine la stimuli chiar când enzima e perturbată → **sistem robust**
- Valoare mică sau negativă = sistem fragil, insulă izolată

### 5.3 Fragmentarea rețelei metabolice cu vârsta
Rețeaua de adaptabilitate a creierului tânăr este:
- Mai distribuită uniform
- Mai interconectată (mai puține componente izolate la același prag de filtrare)
- Mai complexă topologic (mai multe simplexuri direcționate de dimensiune mare)

Creierul îmbătrânit:
- Se fragmentează în „insule" — clustere slab cuplate
- Are centralitate medie mai mică (distanțe mai mari între noduri)
- Are complexitate topologică redusă

**Instrumentar:** autorii folosesc algebraic topology (simplexuri direcționate, Flagser-count) pentru cuantificarea acestor diferențe.

### 5.4 Astrocitul — suport activ, nu pasiv
Observație contraintuitivă față de ipoteza „astrocitului egoist":
- Adaptabilitatea majorității metaboliților **neuronali** scade cu vârsta
- Adaptabilitatea metaboliților **astrocitari** crește cu vârsta
- Interpretare: astrocitul își crește activitatea metabolică pentru a compensa declinul neuronal

Astrocitul este un **organism de suport activ** care detectează stresul neuronal și răspunde compensator.

### 5.5 Naveta lactat (ANLS) — direcționalitate condiționată
Teoria ANLS (astrocyte-to-neuron lactate shuttle) descrie fluxul de lactat de la astrocit la neuron ca sursă energetică alternativă. Modelul arată că:
- În creierul tânăr: ANLS funcționează la toate nivelurile de glucoză testate
- În creierul îmbătrânit: direcționalitatea depinde de nivelul glicemiei și de raportul NAD⁺/NADH

La glucoze scăzute (1.6–5.6 mM): atât neuronul cât și astrocitul **exportă** lactat (inversare ANLS)  
La glucoze moderate (6.6–11.6 mM): ANLS păstrează direcționalitatea  
La glucoze ridicate (12.6–13.6 mM): ambele **importă** lactat

### 5.6 Succinate Dehydrogenase (SDH) — nod diferențial
SDH (Complex II al lanțului de transport electroni) este afectat diferit de îmbătrânire în neuroni vs. astrocite — indicator al cuplării asimetrice TCA-ETC în cele două tipuri celulare.

---

## 6. Factori de transcripție și ținte terapeutice

### 6.1 ESRRA — factorul de transcripție hub
Analiza ChEA3 identifică **ESRRA (Estrogen-Related Receptor Alpha)** ca cel mai conectat factor de transcripție în rețeaua de enzime fragile:
- Reglează funcția mitocondrială, biogeneza și turnover-ul
- Reglează catabolismul lipidic
- Legat de autofagie și răspunsul inflamator NF-κB prin Sirt1
- Expresia sa scade cu îmbătrânirea

Proteinele asociate ESRRA (prin STRING database): HIF1A, Sirt1, HDAC8, PGC1α, PGC1β, MEF2C, NRIP1, NCOA1, TFAM, PERM1 — toate implicate în îmbătrânire și neurodegenerare.

### 6.2 Intervenții strategice identificate (terapia DEN)
Optimizare neghidată (constrained optimization) converge spre:

| Intervenție | Parametru | Direcție |
|---|---|---|
| Dietă | Glucoza sanguină | ↓ |
| Dietă cetogenică | β-hidroxibutirat sanguin | ↑ |
| Exercițiu | Lactat sanguin | ↑ |
| Suplimentare NAD | Pool NAD total | ↑ |
| Modulare redox | Shuttlul NADH citosol-mito | ↑ |
| Farmacologic | Expresia Na⁺/K⁺-ATPase | ↑ |

**Insulina** este un factor comun: activează Na⁺/K⁺-ATPase și scade glicemia simultan.

---

## 7. Principii metodologice transferabile

### 7.1 Validare pe date independente
Autorii validează modelul pe date care **nu** au fost folosite la construcție:
- Răspunsul metabolic la stimuli
- Semnalul BOLD
- OGI
- Bugetul energetic ATP (estimat din componente, comparat cu literatura)

### 7.2 Sensitivitate vs. adaptabilitate
- **Sensitivitate** = cât se modifică un metabolit la perturbarea unui parametru (standard)
- **Adaptabilitate** = cât de diferit răspunde la stimul față de repaus, când un parametru e perturbat (nou)

Adaptabilitatea captează **flexibilitatea dinamică** a sistemului, nu doar sensibilitatea statică.

### 7.3 Perturbarea parametrilor cinetici ca model de damage
Modificarea ±20% a parametrilor cinetici (Km, Ki, kcat) simulează:
- Fosforilare/defosforilare
- Erori de translație
- Daune oxidative
- Misfolding proteic

Este un model generic de „damage molecular" aplicabil oricărui sistem enzimatic.

### 7.4 Resurse și baze de date utilizate
- **Tabula Muris Senis** — single-cell transcriptomics mouse, aging
- **BRENDA** — enzyme kinetics database
- **SABIO-RK** — biochemical reaction kinetics
- **Recon3D** — human metabolism reconstruction (gene-reaction rules)
- **ChEA3** — transcription factor enrichment analysis
- **STRING** — protein-protein interaction networks
- **Flagser-count** — directed simplices computation

### 7.5 Limbaj de implementare recomandat
Autorii aleg **Julia** pentru simularea diferențialelor (pachetul DifferentialEquations.jl):
- Performanță pentru sisteme mari de ODE
- Solver: Rosenbrock-W order 2/3 L-stable (toleranțe 1e-8)
- Analiza și figurile: Python

---

## 8. Limitări cunoscute ale modelului — de avut în vedere

- Nu modelează managementul deșeurilor metabolice (evacuarea lactatului)
- Nu include variații ale disponibilității și transportului oxigenului cu vârsta
- Nu are reglare mecanistică a fluxului sanguin prin activare neuronală
- Nu distinge diferențe sex-specifice
- Nu operează la scară genomică completă
- Datele RNA ca proxy pentru proteine — corelație imperfectă
- Parametrii de scalare a nutrienților sanguini în aging — aproximativi

---

*Document generat: 2025 | Versiune: 1.0*  
*Destinat: banca de cunoștințe biosoft / modelare organism uman*
