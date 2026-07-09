---
order: 3
id_code: '003'
title: World-Model Latent Audit
status: Findings established
domain: Research · Reliability
stack:
  - Python
  - Physics sim
metric: Reconstruction latents <span>underperform</span> matched PCA and random projections on recovering causal variables — the gap tracks the objective.
cardHref: /latent-audit
cardHrefExternal: false
cardAriaLabel: World-Model Latent Audit — read note
isCaseStudy: false
cardPeek: R² 0.992 → 0.716 → −0.175
cardPeekCaption: auditor → pixels → latent
desc:
  - A controlled study of whether learned representations actually capture what causes outcomes. Built a contract-safe harness with stored splits and per-joint consequence targets in a physics simulation, then measured how well different latents recover causally-decisive variables.
heroFigCaption: ''
heroImage: assets/latent_audit_r2.svg
heroImageAlt: 'Bar chart: hidden-mass consequence recovery. Analytic auditor R²=0.992, 12-dim pixel probe R²=0.716, autoencoder latent difference R²=−0.175 — worse than predicting the mean.'
heroImageCredit: ''
heroImageCreditUrl: ''
didNotDo: ''
scopeNotes: ''
---

TODO: user to write
