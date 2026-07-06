# CV master — spine + three lenses

Single source of truth for tailored CV variants. Facts live in `spine.tex`; lenses only change headline, summary, competencies, DCAM bullet emphasis, and skills taxonomy.

## Files

| File | Role |
|------|------|
| `spine.tex` | Fixed facts — canonical titles, experience, education. **Never edited during tailoring.** |
| `cv_lensA_design.tex` | Design / mechanical lens — headline, summary, competencies, DCAM emphasis, skills |
| `cv_lensB_robotics.tex` | Robotics / automation lens |
| `cv_lensC_systems.tex` | Systems / simulation lens |

Each lens file defines `\Headline`, `\Summary`, `\Competencies`, `\AssetCoolBullets`, `\Skills`, etc., then `\input{spine}`.

## Compile

Run from this directory:

```bash
cd notebook/cv
pdflatex cv_lensA_design.tex    # design roles
pdflatex cv_lensB_robotics.tex  # robotics / automation roles
pdflatex cv_lensC_systems.tex   # systems / simulation roles
```

Tailoring = pick a lens, optionally reorder 2–3 bullets in the lens file (not in spine), compile.

Published PDF for sinani.ai: `assets/cv/Uljan_Sinani_CV.pdf` (typically Lens B).

## Regenerate PDF

`pdflatex` is not installed in the Cursor environment. Regenerate locally:

```bash
cd notebook/cv && pdflatex cv_lensB_robotics.tex &&
cp cv_lensB_robotics.pdf ../../assets/cv/Uljan_Sinani_CV.pdf
```

Then commit and push the updated PDF.

---

## ACCURACY RULES (binding)

- The Hydro-Québec DCAM trial ran on a **DECOMMISSIONED** line. Banned in prose: "live", "live-line", "live grid/conductor/power-grid", "energised", "energized". (CSS classes, code identifiers, status badges like "System · live", and quoted prohibitions in `notebook/dcam.md` are exempt.) Correct phrasing: "300 m conductor span on a decommissioned line", "utility grid infrastructure".
- Canonical role titles are FIXED and never tailored:
  - Senior Mechatronics Engineer (AssetCool, May 2025–June 2026);
  - Mechatronics Design Engineer (Federal-Mogul/Tenneco, 2023–2025);
  - Mechatronics Engineer (R&D) (Borg Automotive UK, 2019–2020);
  - Mechatronics Engineer (R&D) (CPI Belgium, 2018–2019);
  - Junior Mechatronics Engineer (BORG Automotive A/S, 2016–2017).
  No "Mechanical Design Engineer" or "Mechanical Engineer" title exists anywhere in this career. Ever.
- DCAM scope per `notebook/dcam.md` "Did NOT do": no embedded electronics, no sensing, no closed-loop control, no "full stack" claims attributed to DCAM. Mechanical design/actuation/fluid delivery + **coordination** with electronics/software teams is the permitted framing.
- Never invent claims, metrics, or evidence links. When unsure, omit.
