# Brain clocks workshop

Materials for the Workshop on Whole-Brain Models and High-Order Interactions for Brain Health.

Carlos Coronel

This package introduces brain-age models and their applications, followed by a hands-on tutorial using gray matter volume (GMV). An EEG exercise is included for independent work.

## Contents

| File | Purpose |
| --- | --- |
| `Part_I.pdf` | Introduction to brain clocks, machine learning, validation and interpretation. |
| `Part_II.pdf` | Applications of brain clocks. |
| `Part_III.pdf` | Slides supporting the hands-on tutorial. |
| `Tutorial/01_GMV_and_groups.ipynb` | Inspect the data and visualize age-adjusted group differences in GMV. |
| `Tutorial/02_GMV_clock.ipynb` | Train a linear SVR age model, evaluate it, calculate BAGs and compare groups. |
| `Tutorial/03_Do_it_yourself.ipynb` | Build an EEG age model and investigate BAGs in relation to education. |
| `Tutorial/brain_age_data.xlsx` | GMV features, age and group labels; sheet: `Participants`. |
| `Tutorial/aperiodic_total_sample.xlsx` | EEG slope features, age, sex and education for the independent exercise. |
| `Tutorial/requirements.txt` | Python libraries and versions. |
| `Tutorial/assets/` | Local AAL atlas, label table, anatomical background and provenance information. |

Use Python 3.12. Open a terminal in the extracted package folder and run:

The first notebooks expect their working directory to be `Tutorial`, beside the Excel files and `assets` folder. If a file is not found, check the working directory with `Path.cwd()`.

Install the libraries before going offline.

## Suggested order

1. Read Part I and Part II for the conceptual background.
2. Use Part III alongside notebooks 1 and 2.
3. Complete notebook 3 independently, using notebook 2 as a guide.

**Just in case: the model fitting can take several minutes. The calibration loop fits many additional models.**

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

Source: *Brain clocks chart genetic risk, staging, mechanisms, and multimodal phenotypes in Down syndrome and Alzheimer's disease*, Nature Aging. The DS participants are a subset of the Barcelona cohort. The tutorial is not a replication of the paper's full analysis.

## Independent EEG exercise

The supplied EEG table contains **1,285 rows and 10 `Slope_` features**, plus `Age`, `Sex` and `Educ`. Use the actual supplied table rather than sample counts from earlier drafts or the full paper.

Source: Hernandez et al. (2024), *Brain health in diverse settings: How age, demographics and cognition shape brain function*, NeuroImage.

Repository: https://github.com/euroladbrainlat/Brain-health-in-diverse-setting
