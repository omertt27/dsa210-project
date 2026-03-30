# DSA 210 – Social Media Use & Mental Health Analysis

> **Social Media Use & Mental Health: A Data-Driven Survey Analysis**  
> A data science project for DSA 210, Spring 2025-2026.

---

## Overview

This project analyzes the relationship between social media usage patterns and mental health outcomes (anxiety, depression, distraction, sleep issues) using a real-world survey dataset of 481 respondents. The goal is to uncover statistically meaningful patterns and build predictive models from survey data collected at a university.

---

## Repository Structure

```
dsa210-project/
│
├── data/
│   ├── raw/               # Raw downloaded CSV datasets
│   └── processed/         # Cleaned & merged datasets
│
├── notebooks/
│   ├── 01_eda.ipynb        # Exploratory Data Analysis
│   ├── 02_hypothesis.ipynb # Hypothesis Testing
│   └── 03_ml_models.ipynb  # Machine Learning Models
│
├── src/
│   ├── data_parser.py      # Loads and validates raw datasets
│   ├── data_cleaner.py     # Cleans and merges datasets
│   └── visualizations.py   # Reusable plotting functions
│
├── proposal.md             # Project proposal
├── report.md               # Final report (due May 18)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## Datasets

| Source | Description | Size | Link |
|---|---|---|---|
| **Social Media & Mental Health (smmh.csv)** | Real survey: age, gender, occupation, daily usage hours, 12 mental health indicators (1–5) | **481 rows, 21 columns** | [Kaggle](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health) |
| Sleep Health & Lifestyle | Sleep duration, quality, stress, physical activity, BMI, disorders | 374 rows | [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) |

Download the datasets from Kaggle and place the CSV files in `data/raw/` before running the notebooks:
- `data/raw/smmh.csv`
- `data/raw/sleep_health.csv`


---

## How to Reproduce the Analysis

### 1. Clone the repository
```bash
git clone https://github.com/omertt27/dsa210-project.git
cd dsa210-project
```

### 2. Download the datasets
- [Social Media Usage & Emotional Well-Being](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being) → save to `data/raw/social_media.csv`
- [Sleep Health and Lifestyle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) → save to `data/raw/sleep_health.csv`

### 3. Set up the Python environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the notebooks in order
```bash
jupyter notebook notebooks/
```
Open and run:
1. `01_eda.ipynb` – Exploratory Data Analysis
2. `02_hypothesis.ipynb` – Hypothesis Tests
3. `03_ml_models.ipynb` – Machine Learning

---

## Timeline

| Date | Milestone |
|---|---|
| Mar 17 | GitHub repo created ✅ |
| Mar 31 | Proposal submitted |
| Apr 14 | Data collection, EDA & hypothesis tests |
| May 5  | ML methods applied |
| May 18 | Final report & code |

---

## Requirements

See [`requirements.txt`](requirements.txt) for full list. Key packages:
- `pandas`, `numpy` – data manipulation
- `matplotlib`, `seaborn` – visualization
- `scipy`, `statsmodels` – hypothesis testing
- `scikit-learn` – machine learning

---

## Academic Integrity

Publicly available, anonymized Kaggle datasets are used. AI tools (GitHub Copilot) were used for boilerplate code generation and are documented in the final report.
