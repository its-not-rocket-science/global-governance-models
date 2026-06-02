# Global Governance Models

A curated dataset of governance systems across world history — spanning ancient, tribal, imperial, feudal, colonial, and modern democratic models. Includes structured data, network visualisations, and a Python script to regenerate all outputs from source.

---

## Overview

Governance systems are one of humanity's most consequential experiments. This dataset attempts to capture the structural properties of those experiments in a form suitable for comparative analysis, computational modelling, and research at the intersection of political science, history, and AI alignment.

The dataset is useful for:

- Comparative politics and historical sociology
- Training or evaluating AI systems on structured knowledge about human institutions
- Research on constitutional design, institutional resilience, and regime transitions
- Input data for game-theoretic models of collective decision-making (see also: [tensor-based-game-theory-identifying-critical-coalitions-climate-change-negotiations](../tensor-based-game-theory-identifying-critical-coalitions-climate-change-negotiations))

---

## Contents

```
global-governance-models/
├── data/
│   ├── governance_systems.csv      # Master dataset: one row per governance system
│   ├── attributes.md               # Data dictionary: all fields defined and sourced
│   ├── transitions.csv             # Regime transitions and their drivers
│   └── actors.csv                  # Key actors and their roles
├── visualisations/
│   ├── timeline.html               # Interactive timeline of governance systems
│   ├── network.html                # Network graph: influence relationships between systems
│   └── comparison.html             # Side-by-side attribute comparison tool
├── scripts/
│   └── regenerate.py               # Regenerates all outputs from source data
└── README.md
```

---

## Dataset fields

Each governance system record includes (see `data/attributes.md` for full definitions and sources):

| Field | Description |
|---|---|
| `system_id` | Unique identifier |
| `name` | Common name of the governance system |
| `period_start` / `period_end` | Approximate dates (BCE/CE) |
| `region` | Geographic region (UNSD subregion classification) |
| `type` | Broad type: tribal, city-state, empire, theocracy, republic, constitutional monarchy, etc. |
| `succession_mechanism` | How leadership transferred: hereditary, election, conquest, appointment, lottery |
| `participation_level` | Estimated proportion of population with political participation |
| `centralisation` | 1–5 scale: highly distributed → highly centralised |
| `rule_of_law` | Presence of codified law and independent adjudication (Y/partial/N) |
| `source` | Primary academic source(s) for this record |

---

## Data sources

All records are sourced from peer-reviewed academic literature. Sources are cited per record in `data/governance_systems.csv`. Key references include:

- Diamond, J. (1997). *Guns, Germs, and Steel*. W. W. Norton.
- Tilly, C. (1990). *Coercion, Capital, and European States*. Blackwell.
- Acemoglu, D. & Robinson, J. (2012). *Why Nations Fail*. Profile Books.
- POLITY IV / V Project (Marshall & Gurr, 2020) — for modern regime scores

**A note on data quality**: historical governance data is inherently uncertain. Records for ancient and prehistoric systems are approximate and should be treated as informed estimates, not precise measurements. The `source` field indicates the provenance of each record; please verify against primary sources before using this data in published research.

---

## Regenerating outputs

```bash
pip install -r requirements.txt
python scripts/regenerate.py
```

This reads `data/governance_systems.csv` and regenerates all visualisations in `visualisations/`.

---

## Licence

Code: MIT.

Data: [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Attribution: Schleiferdyne Systems / `its-not-rocket-science` (GitHub). If you use this dataset in published work, please cite the repository URL and note the data quality caveats above.
