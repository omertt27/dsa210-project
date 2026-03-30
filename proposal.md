# DSA 210 Project Proposal
**Student:** Omer  
**Course:** DSA 210 Introduction to Data Science – Spring 2026  
**Date:** March 31, 2026

---

## Project Title
Social Media Use & Mental Health

---

## Motivation

I spend a lot of time on social media and I've noticed it sometimes affects my mood and focus. I wanted to see if this is backed by data — specifically, whether people who use social media more also report worse mental health indicators like depression, anxiety, and sleep problems.

---

## Dataset

**Source:** Kaggle – [Social Media and Mental Health](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health)  
**File:** `smmh.csv`

This is a real survey collected via Google Forms in April–May 2022, with **481 responses**. The survey has 21 questions covering:

- **Demographics:** age, gender, relationship status, occupation
- **Usage:** average daily time on social media, platforms used
- **Mental health indicators (1–5 scale):** purposeless use, distraction, restlessness, worry, difficulty concentrating, comparing to others, seeking validation, feeling depressed, sleep issues, and more

---

## Planned Analysis

1. **EDA:** Look at distributions of usage and mental health scores, check demographic breakdowns, and explore correlations between usage and well-being indicators.

2. **Hypothesis Testing (4 hypotheses):**
   - H1: Heavy users (>3h/day) have higher mental health risk scores than light users
   - H2: Daily usage time positively correlates with depression sub-score
   - H3: Daily usage time positively correlates with anxiety sub-score
   - H4: Students spend more time on social media than non-students

3. **Machine Learning:**
   - Predict a user's overall mental health risk score (regression)
   - Classify users as high or low mental health risk (classification)
   - Look at feature importance to see which survey answers matter most

---

## Tools

Python, pandas, numpy, matplotlib, seaborn, scipy, scikit-learn — all in Jupyter Notebooks.

---

## Repository
[https://github.com/omertt27/dsa210-project](https://github.com/omertt27/dsa210-project)
