# AIOps — Module 1 Assignment

**Kevin Sona (DA24B007)** 

Submission repository for Assignment 1. This README describes the repository
layout, how to set up the environment, and how to reproduce each question's
results.

Demonstration video at:

---

## Repository structure

```
AIOps-A1/
├── MNIST-MLFlow.ipynb      # Q2 — MLflow experiment sweep and analysis
├── row_count.py            # Q3 — generates files.csv from the data/ directory
├── data.dvc                # Q3 — pointer to the DVC-versioned image dataset
├── files.csv.dvc           # Q3 — pointer to the DVC-versioned manifest
├── Artifacts/              # screenshots and written deliverables
├── requirements.txt        # pinned dependencies
├── .dvc/                   # DVC configuration (remote: S3)
├── report.pdf 
└── README.md

```

`data/`, `files.csv`, `mlruns/`, `mlflow.db`, and `.venv/` are present locally but
excluded from Git — the first two are versioned by DVC, the rest are local state.

### Artifact naming convention

Files in `Artifacts/` are named `<question>.<subpart>` — for example, the
screenshot required by Question 2 part 3 is `2.3`.

---

## Setup

```bash
git clone git@github.com:kevii137/AIOps-A1.git
cd AIOps-A1

python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m ipykernel install --user --name aiops-a1 --display-name "AIOps A1"
```

To retrieve the DVC-tracked data (requires AWS credentials for the S3 remote):

```bash
dvc pull
```

---

## Question 1 — Technical Debt Diagnosis

 Answer in `report.pdf`.

## Question 2 — MLflow Experiment Comparison

**Notebook:** `MNIST-MLFlow.ipynb`

Twelve runs on the full 70k MNIST dataset with an `MLPClassifier`, sweeping three
hyperparameters: learning rate (1e-4, 1e-3, 1e-2), width (64, 128), and depth
(1, 2), at `max_iter=100`.

### Running it

Start the tracking server in a separate terminal, from the repository root:

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
```

Then open **http://localhost:5000** — browse to `localhost`, not `0.0.0.0`, or
the UI will load empty due to a blocked cross-origin request.

Open `MNIST-MLFlow.ipynb`, select the **AIOps A1** kernel, and run all cells.

### Deliverables

| Part | File |
|---|---|
| 2.1 — run-comparison screenshot | `Artifacts/2.1` |
| 2.2 — written analysis (150–250 words) | `Artifacts/2.2` |
| 2.3 — logging code | `Artifacts/2.3` |
\

## Question 3 — DVC Data Versioning & Rollback

**Script:** `row_count.py` — walks `data/` and writes `files.csv`, one row per
image file plus a header.

Remote: S3 bucket (`s3://aiops-kevin-2026/`).

### Versions

| Tag | Dataset | `files.csv` |
|---|---|---|
| `v1` | 1800 images | 1800 rows + header |
| `v2` | 2800 images (after `new-labels.zip`) | 2800 rows + header |


Terminal output proving the row count matches v1 is in `Artifacts/3.3`.

---

## Question 4 — End-to-End Reproducibility Drill

Completed with an assigned partner in a **separate repository**, since it
requires its own commit history and clean handoff:

**Repository:** `https://github.com/Kevii137/AIops-A1Q4`

Partner A's role (train, log with `git_commit` tag, version data with DVC,
register the model) and Partner B's reproduction protocol are documented in that
repository's `README.md` and `PARTNER_B.md`.

---

## Submission

| Item | Location |
|---|---|
| This repository | `https://github.com/Kevii137/AIops-Assignment-1` |
| Q4 repository | `https://github.com/Kevii137/AIops-A1Q4` |
| 1-page PDF write-up | `report.pdf` |
| Demonstration video | `<drive-link>` |

## AI Usage

 1) Writing the script for row_count.py 
 2) Help with modifying lab scripts for MNIST dataset and MLP model
 3) Help with setting up s3
 4) Writing this readme file