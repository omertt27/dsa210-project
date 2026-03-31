# DSA 210 Project Proposal
**Student:** Omer  
**Course:** DSA 210 Introduction to Data Science – Spring 2026  
**Date:** March 31, 2026

---

## Project Title
Social Media Use & Mental Health

---

## Motivation

I spend a lot of time on social media and I've noticed it sometimes affects my mood and focus. I wanted to see if this is actually backed by data — specifically, whether people who use social media more also report worse mental health indicators like depression, anxiety, and sleep problems.

---

## Data Sources

**Primary dataset – Social Media & Mental Health Survey**  
Source: Kaggle – [Social Media and Mental Health](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health)  
File: `smmh.csv` — real survey collected via Google Forms in April–May 2022, **481 responses**, 21 columns covering demographics, daily usage time, platforms used, and 12 mental health indicators rated on a 1–5 scale (distraction, restlessness, depression, anxiety, sleep issues, etc.).

**Enrichment dataset – Sleep Health & Lifestyle**  
Source: Kaggle – [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)  
File: `sleep_health.csv` — **374 records** with sleep duration, sleep quality (1–10), stress level (1–10), physical activity (min/day), BMI category, and sleep disorder diagnosis.

**Planned enrichment:** The two datasets share demographic variables (age group, gender, occupation type). I will use these to join/merge representative sleep and stress statistics into the primary survey data, giving each respondent group an estimated sleep quality and stress context. This enriches the feature space and allows me to ask whether the mental health patterns in the social media survey align with known sleep/stress profiles from the lifestyle dataset.

---

## Planned Analysis

1. **EDA:** Distributions of usage and mental health scores, demographic breakdowns, correlations between usage and well-being indicators, enriched sleep/stress profiles per group.

2. **Hypothesis Testing (4 hypotheses):**
   - H1: Heavy users (>3h/day) have higher mental health risk scores than light users
   - H2: Daily usage time positively correlates with depression sub-score
   - H3: Daily usage time positively correlates with anxiety sub-score
   - H4: Students spend more time on social media than non-students

3. **Machine Learning:**
   - Predict a user's overall mental health risk score (regression)
   - Classify users as high or low mental health risk (classification)
   - Feature importance analysis to identify the strongest predictors

---

## Tools

Python, pandas, numpy, matplotlib, seaborn, scipy, scikit-learn — all in Jupyter Notebooks.

---

## Repository
[https://github.com/omertt27/dsa210-project](https://github.com/omertt27/dsa210-project)
