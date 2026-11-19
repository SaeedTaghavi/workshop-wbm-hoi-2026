# HOI-based digital twins: hands-on tutorial

Workshop on Whole-Brain Models and High-Order Interactions for Brain Health. IFISC, Palma, 19 November 2026.

## Quick start

**Google Colab (recommended):** [Open the notebook from GitHub](https://colab.research.google.com/github/rubenherzog/workshop-wbm-hoi-2026/blob/main/Materials/Ruben_Herzog/HOI_digital_twins_tutorial/NB_tutorial_HDMF_digital_twins.ipynb). In Colab, use **File → Save a copy in Drive** before saving any changes. This opens an independent session and does not modify the author's notebook. Run the setup cell first: it downloads the code and included data from this public GitHub repository.

**Local Jupyter:** Download or clone the [workshop repository](https://github.com/rubenherzog/workshop-wbm-hoi-2026), then run:

```bash
cd workshop-wbm-hoi-2026/Materials/Ruben_Herzog/HOI_digital_twins_tutorial
pip install -r requirements.txt
jupyter notebook NB_tutorial_HDMF_digital_twins.ipynb
```

On first run, the setup cell downloads the published features file used in section 7 (approximately 96 MB) from [flehue/brain_twins_brainlat](https://github.com/flehue/brain_twins_brainlat) into `data/`. Other data are stored directly in this GitHub folder.

Notebook outputs have been cleared to keep the downloadable copy compact; run the cells to recreate the figures. The original scientific code and exercises are retained.

## Contents

| File | Content |
| --- | --- |
| [NB_tutorial_HDMF_digital_twins.ipynb](./NB_tutorial_HDMF_digital_twins.ipynb) | O-information matrix, HDMF, simulated O-information, global fit, regional fit, model features and PCEV |
| [code/DMF_ISP_numba_EandI.py](./code/DMF_ISP_numba_EandI.py) | HDMF simulator |
| [code/BOLDModel.py](./code/BOLDModel.py) | Hemodynamic model |
| [code/calculate_omat.py](./code/calculate_omat.py) | Gaussian-copula O-information matrix |
| [code/calculate_omat_precision.py](./code/calculate_omat_precision.py) | Closed-form O-information matrix |
| [data/metadata_subsample.csv](./data/metadata_subsample.csv) | 60 participants: demographics and fit parameters |
| [data/empirical_omats_subsample.npz](./data/empirical_omats_subsample.npz) | Empirical O-information matrices |
| [data/optimized_SC.npz](./data/optimized_SC.npz) | Diagnosis-group structural connectivity |
| [data/global_fit_all.csv](./data/global_fit_all.csv) | Global-fit parameters |
| [data/exposome_domains.csv](./data/exposome_domains.csv) | Variables in ten exposome domains |
| [data/regional_fit_116_eps0.08_iter40.npz](./data/regional_fit_116_eps0.08_iter40.npz) | Regional-fit example |
| [requirements.txt](./requirements.txt) | Python requirements |

`BOLDModel.py` and `calculate_omat.py` are copied unchanged from [flehue/brain_twins_brainlat](https://github.com/flehue/brain_twins_brainlat). `DMF_ISP_numba_EandI.py` is adapted with a numba-compiled integration loop, downsampling and optional return/initialization of inhibitory weights; its model equations are unchanged.
