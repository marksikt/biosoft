# Knowledge — Bancă de cunoștințe: Modelare organism uman

Acest director conține extrase conceptuale din literatura științifică,
structurate pentru construcția de modele biologice computaționale ale
organismului uman.

---

## Domeniu: Sistemul nervos central

### Documente disponibile

| Fișier | Subiect | Sursă | An |
|---|---|---|---|
| `ngv_metabolism_aging.md` | Metabolism energetic, electrofizologie, sistem vascular, îmbătrânire — sistemul neuro-glio-vascular | Shichkova et al., Frontiers in Science, Blue Brain Project EPFL | 2025 |
| `cns_neural_regeneration.md` | Regenerare neurală în SNC uman — mecanisme inhibitoare, bariere epigenetice, terapii celulare și farmacologice | Kvistad et al., Frontiers in Neurology, Haukeland / Univ. Bergen | 2024 |

---

## Hartă conceptuală — conexiuni între documente

```
ORGANISM UMAN — SNC

┌─────────────────────────────────────────────────────────┐
│             METABOLISMUL ENERGETIC                      │
│        [ngv_metabolism_aging.md]                        │
│                                                         │
│  Neuron <-> Astrocit <-> Capilar                        │
│  ATP / NAD / mitocondrii / Na-K-ATPase                  │
│  Imbatranire -> fragilitate retea metabolica            │
└─────────────────────┬───────────────────────────────────┘
                      | Cuplare energetica
                      v
┌─────────────────────────────────────────────────────────┐
│             REGENERAREA NEURONALA                       │
│        [cns_neural_regeneration.md]                     │
│                                                         │
│  Bariere extrinseci: Nogo-A / CSPGs / cicatrice glial   │
│  Bariere intrinseci: epigenetice / RAGs / TFs master    │
│  Conul de crestere: mitocondrii locale + sinteza prot.  │
│  Remielinizare: OPC -> oligodendrocite mature           │
└─────────────────────────────────────────────────────────┘
```

### Noduri comune între cele două documente

| Concept | În metabolism | În regenerare |
|---|---|---|
| **Mitocondrii** | Producție ATP, compartimentare | Transport la vârful axonului; energie pentru con de creștere |
| **Astrocitul** | Suport metabolic activ al neuronului | Cicatrice glială (inhibitor) + suport paracrin (benefic) |
| **Na⁺/K⁺-ATPase** | Pompa critică pentru potențialul de acțiune | Depolarizată după axotomie → depleție ATP locală |
| **Ca²⁺** | Semnal intracelular general | Declanșator al programului regenerativ (doze-dependent) |
| **BDNF / IGF-1** | Exercițiul → BDNF → efecte anti-aging | Activează PI3K/AKT/mTOR → pro-regenerativ |
| **Inflamație** | Nu modelată direct în NGV | Rol dual critic (M1 inhibitor / M2 regenerativ) |
| **Îmbătrânire** | Fragilitate metabolică crescută | Remielinizare scăzută; OPC afectate |
| **Factori de transcripție** | ESRRA — hub al enzimelor fragile | TFs master (KLF, c-Jun, STAT3) — regulatori ai RAGs |

---

## Convenție pentru documente noi

Fiecare document conține:
1. **Sursă completă** — citare și instituție
2. **Principii fundamentale** — logica sistemului biologic
3. **Subsisteme detaliate** — organizate conceptual, nu bibliografic
4. **Metodologie transferabilă** — instrumente reutilizabile
5. **Conexiuni cu alte documente** — noduri comune explicitate
6. **Limitări** — ce nu acoperă sursa

Nivel de detaliu: **conceptual** (nu parametric numeric).
