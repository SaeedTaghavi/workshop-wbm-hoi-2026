# Brain clocks workshop

Materials for the Workshop on Whole-Brain Models and High-Order Interactions for Brain Health.

Carlos Coronel, PhD - University of Chile - November 2026

This package introduces brain-age models and their applications, followed by a hands-on tutorial using gray matter volume (GMV). An EEG exercise is included for independent work.

## Contents

| File | Purpose |
| --- | --- |
| `Part_I.pdf` / `Part_I.pptx` | Introduction to brain clocks, machine learning, validation and interpretation. |
| `Part_II.pdf` / `Part_II.pptx` | Applications of brain clocks. |
| `Part_III.pdf` / `Part_III.pptx` | Slides supporting the hands-on tutorial. |
| `Tutorial/01_GMV_and_groups.ipynb` | Inspect the data and visualize age-adjusted group differences in GMV. |
| `Tutorial/02_GMV_clock.ipynb` | Train a linear SVR age model, evaluate it, calculate BAGs and compare groups. |
| `Tutorial/03_Do_it_yourself.ipynb` | Build an EEG age model and investigate BAGs in relation to education. |
| `Tutorial/brain_age_data.xlsx` | GMV features, age and group labels; sheet: `Participants`. |
| `Tutorial/aperiodic_total_sample.xlsx` | EEG slope features, age, sex and education for the independent exercise. |
| `Tutorial/requirements.txt` | Python libraries and versions. |
| `Tutorial/assets/` | Local AAL atlas, label table, anatomical background and provenance information. |

The `.ipynb_checkpoints` folder contains Jupyter backup copies. Open the notebooks listed above, not the checkpoint files.

## Setup

Extract the ZIP before opening the notebooks. Keep the folder structure unchanged.

Use Python 3.12. Open a terminal in the extracted package folder and run:

```text
cd Tutorial
python -m venv .venv
```

On Windows:

```text
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m ipykernel install --user --name brain-clocks --display-name "Python (brain clocks)"
.venv\Scripts\python.exe -m jupyterlab
```

On macOS or Linux:

```text
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name brain-clocks --display-name "Python (brain clocks)"
.venv/bin/python -m jupyterlab
```

Select the **Python (brain clocks)** kernel. Run each notebook from top to bottom. Each notebook loads its own data; running notebook 1 does not populate notebook 2's variables.

The first notebooks expect their working directory to be `Tutorial`, beside the Excel files and `assets` folder. If a file is not found, check the working directory with `Path.cwd()`.

Install the libraries before going offline. Once installed, the supplied data, atlas and background image can be used without internet. External links require a connection. The package does not include Python or offline library installers.

## Suggested order

1. Read Part I and Part II for the conceptual background.
2. Use Part III alongside notebooks 1 and 2.
3. Complete notebook 3 independently, using notebook 2 as a guide.

Model fitting can take several minutes. The calibration loop fits many additional models. Saved notebook outputs can be viewed without rerunning cells; they may need updating after any code or data changes.

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

Notebook 1 checks the data and treats nonpositive GMV values as missing in its analysis copy. It calculates CN-referenced z-scores for descriptive maps. For each ROI, it compares AD with CN and pooled DS with CN, adjusting for age within the age range shared by each pair. Map colors show all estimated coefficients, not only significant results; FDR-adjusted p-values are calculated separately. These are cross-sectional differences, not measured longitudinal atrophy.

Notebook 2 reads the Excel table independently and does not carry over notebook 1's cleaning. The supplied table contains 30 nonpositive GMV cells; inspect these before extending the analysis. Changes to data handling require rerunning the model and its outputs.

## Brain-age workflow

Notebook 2 uses a `StandardScaler` followed by `LinearSVR` with squared epsilon-insensitive loss.

- Train and evaluate the reference clock using CN only.
- Use 5-fold CV repeated 10 times, with seed 1234.
- Fit scaling inside each training fold.
- Explore C using validation MAE. The baseline BAG analysis uses fixed C = 1 and epsilon = 3 years.
- Obtain each CN prediction from its held-out fold. Predict the other groups with each fitted outer model.
- Estimate age-bias correction from internal out-of-fold predictions within each outer training set. This internal CV is for calibration, not hyperparameter tuning.
- Calculate raw BAG as predicted age minus chronological age, then subtract the expected age-related bias.
- Average repeated predictions and corrected BAGs within participant before group analysis. Repetitions are not additional subjects.
- Measure feature importance by shuffling individual ROIs in held-out CN data and recording the increase in MAE. This measures usefulness for age prediction, not causation or disease specificity.
- Compare corrected BAGs using an age-adjusted group model, HC3 robust standard errors and Holm-adjusted group-versus-CN p-values.

The included ANCOVA is additive and assumes a common age slope across groups. An age-by-group interaction is discussed but is not fitted by the supplied formula. The boxplots show observed corrected BAG distributions, not adjusted group means.

Validation curves are exploratory. Selecting a new C using those curves and reporting the same CV scores does not provide an independent evaluation of tuning. Use nested tuning CV or a separate test set for that purpose.

## Independent EEG exercise

The supplied EEG table contains **1,285 rows and 10 `Slope_` features**, plus `Age`, `Sex` and `Educ`. Use the actual supplied table rather than sample counts from earlier drafts or the full paper.

Source: Hernandez et al. (2024), *Brain health in diverse settings: How age, demographics and cognition shape brain function*, NeuroImage.

Repository: https://github.com/euroladbrainlat/Brain-health-in-diverse-setting

Tasks:

1. Inspect the data and standardize features within training folds.
2. Predict age using only the slope features, with 5-fold CV repeated 10 times.
3. Report held-out MAE, R2 and the age-prediction correlation.
4. Calculate raw and corrected BAGs using training-only calibration.
5. Test the BAG-education association while controlling for age, or compare low and high education using P33 and P66. Keep the middle group in clock training and exclude it only from the low-high comparison.

Keep education, sex and any exported index out of the age-model predictors. Use education values from 0 to 30 years for the education analysis. If tuning hyperparameters, keep tuning inside the outer training data. A null association is a valid result.

You may use your own dataset instead. It should contain brain features and age, with education available if you wish to address the same question.

## Interpretation

A positive BAG means the model predicts an older age than the participant's chronological age. It does not by itself establish disease, accelerated aging or clinical usefulness. A rate of aging requires longitudinal evidence. Age-bias correction is a statistical adjustment, not biological validation.

The atlas and anatomical background are bundled locally. Their sources are listed in `Tutorial/assets/PROVENANCE.txt`. Consult the original data sources and their terms before redistributing or reusing the datasets outside the workshop.
