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

## Known inconsistencies (not yet resolved in spine)

- **Borg Automotive UK:** site/notebook use *Mechatronics Engineer (R&D)*; `spine.tex` lists *Mechanical Design Engineer*.
- **DCAM scope:** lens bullets may claim sensing/embedded control; see `notebook/dcam.md` § Did NOT do (binding) before using those bullets verbatim.

---

## ACCURACY RULES (binding, from notebook/)

- The Hydro-Québec DCAM trial ran on a DECOMMISSIONED line. The words "live", "live-line", "live grid", "live conductor", "energised/energized infrastructure" are BANNED in any career/CV/site content. Correct phrasing: "300 m conductor span on a decommissioned line", "utility grid infrastructure".
- Canonical role titles are FIXED and never tailored:
  - Senior Mechatronics Engineer (AssetCool, Leeds, May 2025–June 2026);
  - Mechatronics Design Engineer (Federal-Mogul/Tenneco, Essex, 2023–2025);
  - Mechatronics Engineer (R&D) (Borg Automotive UK, 2019–2020);
  - Mechatronics Engineer – R&D (CPI, Belgium, 2018–2019);
  - Junior Mechatronics Engineer (BORG Automotive A/S, Denmark, 2016–2017).
- Job descriptions describe what was actually done. Never inflate, never invent metrics, never add tools not listed. When unsure, omit.
- No new frameworks, dashboards, or extra pages beyond what is asked.
