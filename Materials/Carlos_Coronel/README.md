# Brain clocks workshop

Materials for the Workshop on Whole-Brain Models and High-Order Interactions for Brain Health.

Carlos Coronel

This package introduces brain-age models and their applications, followed by a hands-on tutorial using gray matter volume (GMV). An EEG exercise is included for independent work.

## Contents

| File | Purpose |
| --- | --- |
| `Talk.pdf` | Introduction to brain clocks, machine learning, validation, interpretation and applications. |
| `Tutorial.pdf` | Slides supporting the hands-on tutorial. |
| `Tutorial/01_GMV_and_groups.ipynb` | Inspect the data and visualize age-adjusted group differences in GMV. |
| `Tutorial/02_GMV_clock.ipynb` | Train a linear SVR age model, evaluate it, calculate BAGs, compare groups and explore feature importance. |
| `Tutorial/03_Do_it_yourself.ipynb` | Build an EEG age model and investigate BAGs in relation to education. |
| `Tutorial/brain_age_data.xlsx` | GMV features, age and group labels; sheet: `Participants`. |
| `Tutorial/aperiodic_total_sample.xlsx` | EEG slope features, age, sex and education for the independent exercise. |
| `Tutorial/requirements.txt` | Python libraries and versions. |
| `Tutorial/assets/` | Local AAL atlas, label table, anatomical background and provenance information. |

## Setup

Use Python 3.12. Extract the package and keep its folder structure unchanged.

Open a terminal in the extracted package folder and run:

```text
cd Tutorial
python -m pip install -r requirements.txt
python -m jupyterlab
```

Run each notebook from top to bottom. Each notebook loads its own data.

The notebooks expect their working directory to be `Tutorial`, beside the Excel files and `assets` folder. If a file is not found, check the working directory with `Path.cwd()`.

Install the libraries before going offline. The data and atlas files are included locally.

## Suggested order

1. Read `Talk.pdf` for the conceptual background and applications.
2. Use `Tutorial.pdf` alongside notebooks 1 and 2.
3. Complete notebook 3 independently, using notebook 2 as a guide.

**Model fitting and permutation analyses can take several minutes. Saved outputs can be viewed without rerunning the notebooks.**

## GMV data

The supplied table contains **6,909 records and 90 cerebral AAL ROI features**. Cerebellar regions are excluded. Columns beginning with `G_` are GMV features.

| Group | Meaning | Records |
| --- | --- | ---: |
| CN | Cognitively normal controls | 4,715 |
| AD | Alzheimer's disease | 2,032 |
| aDS | Asymptomatic Down syndrome | 92 |
| pDS | Prodromal Down syndrome | 27 |
| dDS | Down syndrome with dementia | 43 |

Volumes were already normalized by total intracranial volume (TIV). The Excel table retains those values; standardization is performed in Python. Age is the demographic covariate used in this tutorial.

Source: *Brain clocks chart genetic risk, staging, mechanisms, and multimodal phenotypes in Down syndrome and Alzheimer's disease*, Nature Aging.

The DS participants are a subset of the Barcelona cohort. The tutorial is not a replication of the paper's full analysis.

## Independent EEG exercise

The supplied EEG table contains **1,285 rows and 10 `Slope_` features**, plus `Age`, `Sex` and `Educ`.

Use the slope features to predict age, evaluate held-out performance and calculate BAGs. Then investigate their association with education while controlling for age, or compare low- and high-education groups.

Source: Hernandez et al. (2024), *Brain health in diverse settings: How age, demographics and cognition shape brain function*, NeuroImage.

Repository: https://github.com/euroladbrainlat/Brain-health-in-diverse-setting
