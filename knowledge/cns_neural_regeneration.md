# Banca de cunoștințe — Regenerare neurală în SNC uman

**Sursă:** Kvistad CE, Kråkenes T, Gavasso S, Bø L (2024). *Neural regeneration in the human central nervous system — from understanding the underlying mechanisms to developing treatments. Where do we stand today?*  
Frontiers in Neurology, 15:1398089. doi: 10.3389/fneur.2024.1398089  
**Neuro-SysMed, Haukeland University Hospital / University of Bergen, Norvegia**  
**Extras pentru:** modelare organism uman — nivel conceptual

---

## 1. Principiu fundamental — de ce nu se regenerează SNC-ul matur

### 1.1 Trade-off evolutiv
Incapacitatea de regenerare a SNC-ului matur nu este un defect, ci un **compromis evolutiv deliberat**: complexitatea rețelelor neuronale mature impune stabilitate, iar creșterea axonală necontrolată ar produce conexiuni ectopice, sinapse aberante, durere neuropatică și epilepsie.

Dovadă: SNC-ul peștilor și amfibienilor se poate regenera — complexitatea redusă permite acest lucru. Mamiferele au ales complexitate în detrimentul regenerării.

### 1.2 Distincția esențială: SNC vs. SNP
Aceasta este distincția de bază a întregului domeniu:

| Caracteristică | SNC (matur) | SNP |
|---|---|---|
| Regenerare axonală | Absentă / minimă | Prezentă |
| Mediu inhibitor | Puternic | Permisiv |
| Program genetic de regenerare | Inactiv | Activ după leziune |
| Barieră epigenetică | Prezentă | Depășită după leziune |
| Clearance mielină | Lent (microglia) | Rapid (macrofage + celule Schwann) |

### 1.3 Neuronii fetali vs. maturi — proba cheie
Transplantul de neuroni fetali în modele de SCI: celulele imature supraviețuiesc, axonii traversează leziunea și formează sinapse. Neuronii maturi nu fac același lucru.

Concluzie: există un **comutator intraneural** care se dezactivează în cursul maturizării, când axonii ajung la țintele lor și formează sinapse. Maturizarea = renunțarea la programul de creștere în favoarea activității sinaptice.

---

## 2. Bariere extrinseci ale regenerării

### 2.1 Proteinele mielinei — calea RhoA/ROCK
Oligodendrocitele mature produc molecule inhibitoare ale creșterii axonale:
- **Nogo-A** — principalul inhibitor, acționează prin receptorul Lingo-1
- **MAG** (myelin-associated glycoprotein)
- **OMgp** (oligodendrocyte myelin glycoprotein)

Toate trei converg pe aceeași cale:
```
Nogo-A / MAG / OMgp → Lingo-1 → RhoA-GTP → ROCK → 
inhibiție citoschelet → colaps con de creștere → fără regenerare
```

**Observație importantă:** Deletarea simultană a tuturor trei (Nogo + MAG + OMgp) la șoareci knock-out nu a produs regenerare semnificativă — există mecanisme suplimentare.

### 2.2 Cicatricea glială — rol dual
Astrocitele reactive migrează la marginea leziunii, proliferează și secretă moleculele de matrice extracelulară pentru a forma **cicatricea glială**:

**Funcție protectoare:** izolează inflamația, protejează țesutul sănătos adiacent  
**Funcție inhibitoare:** barieră fizică și chimică pentru regenerarea axonală

Principalii inhibitori din cicatrice: **CSPGs** (chondroitin sulphate proteoglycans) — acționează prin aceeași cale Rho/ROCK ca proteinele mielinei.

**Nuanță critică:** Prevenirea formării cicatricii → leziune mai mare, outcome mai rău. Heterogenitatea astrocitelor: unele tipuri de CSPG (CSPG4, CSPG5) *susțin* regenerarea axonală. Nu toate componentele cicatricii sunt inhibitoare.

### 2.3 Inflamația — sabie cu două tăișuri
**Efecte pro-inflamatorii (dăunătoare):**
- Microglia M1: citokine citotoxice, extinderea leziunii
- Macrofagele periferice: contribuie la mediul inhibitor acut

**Efecte pro-regenerative (benefice):**
- Microglia M2: factori neurotrofici, diferențiere oligodendrocite, remielinizare
- Clearance detritus: esențial înainte de orice regenerare (fără curățare, fără creștere)
- Macrofagele și celulele Schwann curăță mielina mai eficient decât microglia în SNC

**Principiu pentru modelare:** M1/M2 sunt polii unui spectru, nu categorii discrete.

---

## 3. Bariere intrinseci ale regenerării

### 3.1 Gene asociate regenerării (RAGs)
În SNP, leziunea axonală declanșează o cascadă coordonată de expresie genică — **RAGs** (regeneration-associated genes):
- Enzime metabolice
- Proteine citoscheletale
- Molecule de adeziune

**În SNC, această cascadă nu se activează după leziune.**

Nu toate RAGs promovează regenerarea — unele (ex. SOCS3) o inhibă. Spectrul de gene activate în SNP este larg și nu complet înțeles.

### 3.2 Factori de transcripție master regulatori
Unii TFs reglează mulți RAGs simultan. Deletarea lor reduce regenerarea mai mult decât deletarea RAGs individuale:

| TF | Rol |
|---|---|
| KLF (Krüppel-like factors) | Familie importantă de reglatori ai programului regenerativ |
| c-Jun | Activat în SNP, absent în SNC după leziune |
| STAT3 | Master TF, activat de DLK downstream |
| AKT | Integrator al semnalelor de creștere |
| REST/NRSF | Supresor upstream al programului pro-regenerativ în SNC |

**39 TFs** identificați ca regulatori master pentru ~400 căi de semnalizare în regenerarea senzorială periferică; **23 TFs** suplimentari identificați ulterior.

Programul regenerativ orchestrat de TF master se inițiază numai după leziune SNP, **nu** după leziune SNC.

### 3.3 Bariera epigenetică — mecanismul central
Aceasta este probabil cea mai importantă barieră intrinsecă:

**În SNP după leziune:**
```
Leziune → influx Ca²⁺ → export nuclear HDAC5 → 
HATs acetilează histonele → RAGs accesibile pentru TFs → regenerare
```

**În SNC după leziune:**
```
Leziune → HDAC rămâne în nucleu → 
fără acetilare → RAGs inaccesibile → fără regenerare
```

Bariera epigenetică există și în SNP, dar este **depășită** prin modificări epigenetice induse de leziune. Bariera din SNC apare în cursul maturizării neuronale.

Mecanisme epigenetice implicate:
- **Acetilarea histonelor** (HAT/HDAC) — cel mai studiat
- **Metilarea DNA** — TET enzimele (demtilaze) necesare pentru expresia RAGs; TET3 în SNP, TET1 în SNC experimental
- **PCAF** (HAT) — activat după leziune SNP; overexpresia sa promovează regenerarea senzorială în SCI

### 3.4 Reglarea post-transcripțională — miRNA
miRNA-urile (~22 nucleotide) reglează expresia genică post-transcripțional și pot modula simultan multiple gene:

| miRNA | Efect |
|---|---|
| miR-21 | ↑ 7x după leziune periferică; promovează creșterea neuritelorA |
| miR-26a | Mediază regenerarea senzorială; suprimă GSK3β și PTEN |
| miR-133b | Promovează creșterea neuritelorA; țintește RhoA inhibitor |

Deletarea Dicer (enzimă esențială pentru asamblarea miRNA) → regenerare axonală afectată.

---

## 4. Evenimente intra- și extracelulare necesare pentru regenerare

### 4.1 Semnalizarea leziunii — două faze
Comunicarea de la locul leziunii la soma și nucleu se face în două faze:

**Faza 1 — rapidă:**
- Val retrogradă de Ca²⁺: ~1 mm/min
- Influx Ca²⁺ la vârful axonului secționat + deschidere canale Na⁺ voltage-dependente
- Roluri: resigillarea membranei, asamblarea conului de creștere, activare TFs

**Faza 2 — lentă:**
- Transport retrograd de molecule de semnalizare (ex. DLK)
- Dependent de Ca²⁺; senzor pentru leziunea axonală și destabilizarea citoscheletului
- Downstream → activare TFs JUN și STAT3 → expresie RAGs

**Atenție:** Ca²⁺ este o sabie cu două tăișuri — niveluri excesive declanșează mecanisme autodestructive (depolimerizare citoschelet, apoptoză).

### 4.2 Formarea conului de creștere
Diferența fundamentală SNC vs. SNP:
- **SNP:** axonul secționat formează con de creștere în 3–24h
- **SNC:** se formează bulb de retracție (microtubuli dezorganizați, mitocondrii și vezicule acumulate)

Bulburi de retracție identificate la oameni la >40 ani după SCI.

Structura conului de creștere funcțional:
- Zona periferică (actină): lamelipodii și filopodii — senzori ai micromediului
- Zona centrală (microtubuli): structura rigidă
- Zona de tranziție dinamică: interacțiunea celor două domenii

**Microtubulii** sunt esențiali. Stabilizarea lor (Taxol/epothilone B) → formare con de creștere, prevenire cicatrice, regenerare axonală. Destabilizarea → transformarea conurilor în bulburi de retracție.

### 4.3 Blocuri de construcție și energie
Regenerarea necesită materie primă și energie:

**Sinteza proteică locală:**
- În SNP: mRNA și ribozomi prezenți în axonii distali → sinteză locală de actină, GAP-43, proteine de semnalizare (STAT3, vimentin pentru semnalizare retrogradă)
- În SNC: capacitate translațională locală redusă — **factor restrictiv important**
- Dar: când axonii SNC sunt plasați într-un mediu permisiv (grefon de nerv periferic), aceștia pot conține atât mRNA de creștere cât și componente ribozomale

**Energia:**
- Axotomia depolarizează mitocondriile și epuizează ATP local
- Mitocondriile se concentrează la vârful axonului în regenerare (produc energia necesară)
- 20–30% din mitocondriile neuronale sunt motile (transport bidirecțional)
- Complexul motor/adaptor: **Miro** (RhoT1/2) + **Milton** (TRAK1/2) — leagă mitocondriile de microtubuli
- **Syntaphilin** — imobilizează mitocondriile (efect inhibitor indirect)
- Mobilitatea mitocondriilor este mai redusă în neuronii maturi → barieră intrinsecă suplimentară

### 4.4 Elongarea axonală și formarea sinapselor
**Molecule de ghidare:**
- Attractante (verzi): netrins, factori neurotrofici
- Repulsive (roșii): semaphorine, proteine Wnt, Ryk receptor

**Observație importantă:** Unele molecule de ghidare au efect **opus** în SNC matur față de SNC embrionar. Exemplu: Semaphorin3A este repulsivă pentru neuroni DRG embrionari, dar promovează creșterea în cei maturi.

**Wnt** — exemplu de reexpresie inhibitorie: dirijează axonii în jos în dezvoltare (gradient descendent); se reexprimă după leziunea SNC matur și inhibă regenerarea prin receptorul Ryk.

**Principiu pentru terapie combinatorie:**
Nu este suficientă eliminarea inhibiției — trebuie și atracție chimică la distanță. Studiul Anderson et al. (Nature, 2018) pe SCI complet la șoarece/șobolan combină:
1. Boost capacitate intrinsecă de creștere (osteopontin + IGF-1 + CTNF)
2. Substrat de creștere în cavitate (FGF2 + EGF)
3. Chemoatracție dincolo de leziune (GDNF)

Rezultat: regenerare propriospinală robustă, contacte sinaptice, conducere electrofizologică — dar *fără* îmbunătățire locomotorie spontană. Concluzie: **reabilitarea este componentă obligatorie**.

### 4.5 Remielinizarea — condiție necesară dar insuficientă
Fără remielinizare, regenerarea axonală nu aduce beneficii clinice susținute:
- Mielina menține viteza de conducere nervoasă și suportul metabolic al axonului
- Mielina nouă este mai subțire, mai scurtă și mai vulnerabilă decât cea developmentală
- Remielinizarea = neuroprotecție (previne degenerarea axonală)

**OPCs (oligodendrocyte progenitor cells):**
- 5–8% din populația celulară a SNC
- Proliferează, migrează la locul leziunii, se diferențiază în oligodendrocite mature
- Prezente în leziunile cronice MS, dar **incapabile să se diferențieze** (OPCs ajung prea târziu, în număr insuficient)
- Debris-ul de mielină conține inhibitori ai diferențierii OPC → clearance-ul este condiție prealabilă
- Microglia cu capacitate fagocitică redusă (cu vârsta) → remielinizare scăzută în MS progresivă

---

## 5. Căi intracelulare cheie pentru regenerare

### 5.1 PI3K/PTEN/mTOR
```
Factori de creștere (BDNF, NT-3) → PI3K → PIP2→PIP3 → AKT →
inhibiție TSC1/TSC2 → activare mTOR → sinteză proteică, creștere celulară, regenerare axonală
```
**PTEN** inhibă această cale → scade mTOR → inhibă regenerarea.  
Deletarea PTEN → regenerare axonală robustă (dar risc oncogen — problemă clinică).

### 5.2 RhoA/ROCK
Element de legătură între factorii extrinseci (Nogo, MAG, OMgp, CSPGs) și răspunsul intrinsec:
- În neuroni: RhoA restricționează creșterea axonală (previne protrucția microtubulilor)
- În astrocite: RhoA restricționează astroglioza și producția de CSPG

**Problemă terapeutică crucială:** blocarea RhoA în neuroni → pro-regenerativ; în astrocite → pro-inflamator/pro-glioză. Efecte opuse în același mediu.

### 5.3 Alte căi relevante (enumerate)
- **GSK3β/CRMP2** — reglarea citoscheletului
- **JAK/STAT** — semnalizare inflamatorie și regenerativă
- **DLK/JNK/cJUN** — senzor de leziune axonală, inițiere RAGs
- **cAMP/PKA/CREB** — modulator al pragului de creștere

---

## 6. Patofizologia leziunilor SNC — cadru pentru modelare

### 6.1 Leziunea măduvei spinării (SCI)
**Faza acută:** leziune mecanică → leziune axonală + disrupție microvasculară + influx macrofage/neutrofile/limfocite → edem → necroză  
**Faza subacută:** inflamație + excitotoxicitate + autoreglare vasculară afectată → pierdere neuroni și oligodendrocite (poate depăși impactul inițial)  
**Faza cronică:** fagocitoză detritus → cavitații chistice + benzi subțiri de țesut conjunctiv + cicatrice glială matură

### 6.2 Scleroza multiplă (MS)
- Boală imuno-mediată; leziuni demielinizante multifocale
- T și B limfocite infiltrante; oligodendrocite pierdute
- **Remielinizare spontană** în fazele inițiale → mielină subțire, axoni vulnerabili
- **Leziuni smouldering:** inel de microglie activată în expansiune în jurul ariei inactive demielinizate
- Inflamație meningeală cronică → daune subpiale → neurodegenerare în MS progresivă
- Virusul Epstein-Barr: cauza declanșatoare (mimicry epitop)

### 6.3 Accidentul vascular cerebral ischemic (IS)
- Cheag arterial → ischemie → depleție ATP → influx ionic și acvatic → depolimerizare membrană celulară  
- Radicali liberi → daune ADN și celulare  
- **Penumbra ischemică:** țesut cu hipoxie moderată, apoptoză posibilă (nu necroză) — fereastră terapeutică  
- Astrocite și microglie activate → cicatrice glială → compartimentalizarea leziunii

---

## 7. Intervenții terapeutice — starea curentă a trialurilor clinice

### 7.1 Terapii celulare

**Celule stem neurale (NSC):**
- Auto- sau allo-genic (țesut fetal) sau prin reprogramare celulară
- Mecanism principal: **paracrin** (secretom) — nu transdiferențiere în neuroni funcționali
- Factori secretați: NGF, BDNF, HGF, VEGF + exozomi cu mRNA și miRNA
- Pot stimula celulele stem neurale endogene

**Celule stem mezenchimale (MSC):**
- Prezente în aproape toate țesuturile; heterogene, fără marker unic
- Avantaje: autolog, fără imunosupresie necesară, fără modificare genetică
- Mecanism: imunomodulare (shift M1→M2 microglie) + secretom neurotrofic
- **Problem major:** administrate IV, se prind în plămâni (first-pass pulmonar) — nu ajung în SNC

**Rezultate trialuri clinice (sinteză):**

| Afecțiune | Celule | Rezultat |
|---|---|---|
| SCI | NSC intramedulare | Siguranță demonstrată; eficacitate clinică absentă |
| SCI | MSC intratecale/i.v. | Siguranță; senzație tactilă ușor îmbunătățită; fără efect motor |
| MS | MSC i.v. (n=144, RCT) | Fără diferență față de placebo (leziuni Gd+) |
| MS | MSC intratecal | Semnificativ mai puțini pacienți cu activitate de boală; EDSS îmbunătățit |
| MS | NSC intratecale (faza I) | Siguranță; posibil efect neuroprotector (atrofie ↓, factori neurotrofici ↑ în LCR) |
| IS | MSC i.v. (multiple RCT) | Fără eficacitate clinică consistentă |
| IS | NSC stereotactic | Siguranță; ameliorări modeste în studii mici |

### 7.2 Agenți farmacologici

**VX-210 (inhibitor Rho):**
- Derivat din enzima bacteriană C3 transferaza; inactivează Rho covalent
- Trial fazăI/II, SCI acut: siguranță demonstrată, sugestie de îmbunătățire motorie la SCI cervical
- Trial mai mare (SPRING): terminat prematur — criterii de futilitate îndeplinite
- Primul trial randomizat care a testat un inhibitor al factorilor inhibitori ai regenerării

**ATI355 (anticorp anti-Nogo-A):**
- SCI acut/subacut; administrare intratecală; 52 pacienți
- Concentrație în LCR suficientă; tolerabilitate bună
- Fără îmbunătățiri clinice față de date istorice

**Chondroitinase ABC:**
- Enzimă care digeră CSPG → permite creșterea axonală în modele animale
- Nu a ajuns încă la trialuri clinice umane la scară largă

**Opicinumab (anti-Lingo-1):**
- MS; promovează diferențierea OPC și remielinizarea
- Trial faza II (>400 pacienți): fără îmbunătățire liniară cu doza; doze mici (10, 30 mg/kg) suggestive, doza mare (100 mg/kg) ineficientă
- Posibilă explicație: doza prea mare diferențiază OPC-urile prematur, înainte de migrare

**Clemastine (antihistaminic):**
- Efect antimuscarinic off-target → diferențiere OPC → remielinizare
- Trial faza II (RR-MS, neuropatie optică): reducere semnificativă a latenței PEV → efect remielinizant
- Braț în trial pe MS progresivă terminat — 3 pacienți cu agravare a dizabilității
- Mecanism posibil negativ: inflamație innată via receptorul purinergic P2RX7 în microglie/oligodendrocite
- **Lecție:** efecte opuse în MS recurentă vs. progresivă

**Cerebrolysin (IS):**
- Amestec de peptide neurotrofice; mecanism: neurogeneza (via sonic hedgehog) + reducere radicali liberi
- Trial exploratoriu (208 pacienți): îmbunătățire funcție membru superior; follow-up negativ
- Meta-analiză (1.417 participanți): fără beneficiu clinic demonstrat

**G-CSF (IS):**
- Stimulează eliberarea celulelor mieloide și stem hematopoietice din măduva osoasă
- Potențial efect pro-regenerativ via receptori G-CSF pe celule progenitoare neurale
- Trial faza IIb (328 pacienți): fără eficacitate; tendință spre mai multe SAE

### 7.3 Biomateriale (SCI)
- Schele polimerice biodegradabile → prevenirea cavitației chistice, mai puțină cicatrice, creștere axonală prin scaffold
- Trial clinic (19 pacienți, Neuro-Spinal Scaffold): sigur și bine tolerat; comparativ cu date istorice — 32% conversie la leziune motorie incompletă (vs. ≤17% istoric)
- Necesită trial placebo-controlat

---

## 8. Principii metodologice și lecții din trialurile clinice

### 8.1 De ce eșuează traducerea din modele animale
1. **Complexitate biologică insuficient înțeleasă** — mecanismele moleculare exacte ale eșecului regenerativ nu sunt complet cunoscute
2. **Metodologie preclinică slabă** — modele animale tinere, boală indusă uniform (vs. heterogenitate umană reală)
3. **Putere statistică insuficientă** — populația umană heterogenă necesită studii mai mari
4. **Nicio intervenție singulară nu este suficientă** — barierele sunt multiple și robuste

### 8.2 Principiul combinatoriu — esențial
Concluzia majoră a literaturii: regenerarea semnificativă în SNC necesită **combinarea simultană** a:
1. Eliminarea inhibiției extrinseci (Nogo, CSPG, cicatrice glială)
2. Activarea programului intrinsec de creștere (PTEN↓, mTOR↑, TFs)
3. Suport energetic și material local (mitocondrii, sinteza proteică)
4. Chemoatracție la distanță (GDNF, factori neurotrofici)
5. Remielinizare (OPC diferențiați)
6. Reabilitare și reorganizare de circuit

**Fără reabilitare, chiar și regenerarea anatomică reușită nu produce beneficii funcționale.**

### 8.3 Interferenze între ținte terapeutice — atenție la efecte opuse
RhoA este cel mai bun exemplu: blocarea sa în neuroni este pro-regenerativă, dar în astrocite este pro-inflamatorie. Orice intervenție sistemică poate avea efecte antagoniste în celule diferite din același mediu.

### 8.4 Frontiere viitoare
- **CRISPR** — editare genică pentru modularea programului regenerativ
- **Exozomi** (artificiali sau derivate din celule stem) — livrare de miRNA pentru imunomodulare și regenerare
- **Stimulare electrică** — pentru remielinizare
- **Interfețe creier-coloană** (brain-spine interface) — stimulare epidurală; pacient cu SCI incomplet cervical a recuperat mers pe scări și teren complex
- **Interfețe creier-computer** — control cognitiv al dispozitivelor electronice

---

## 9. Conexiuni cu metabolismul energetic cerebral (document complementar)

Acest document se completează cu `ngv_metabolism_aging.md`:

| Temă | NGV metabolism | CNS regenerare |
|---|---|---|
| Mitocondrii | Producție ATP, compartimentare | Transport la vârful axonului regenerant; esențiale pentru conul de creștere |
| Na⁺/K⁺-ATPase | Pompa critică pentru potențial de acțiune | Depolarizare după axotomie → depleție ATP |
| Astrocitul | Suport metabolic activ al neuronului | Cicatrice glială (inhibitor) + suport paracrin (benefic) |
| Inflamație | Nu modelată direct | Rol dual critic M1/M2 |
| Ca²⁺ | Semnal intracelular | Declanșator al programului regenerativ (doze-dependent) |
| Factori neurotrofici (BDNF, IGF-1) | Exercițiu → creștere BDNF | Activează PI3K/AKT/mTOR pro-regenerativ |
| Îmbătrânire | Fragilitate metabolică crescută | Remielinizare scăzută, OPC afectate, modele animale vs. umani vârstnici |

---

*Document generat: 2025 | Versiune: 1.0*  
*Destinat: banca de cunoștințe biosoft / modelare organism uman*
