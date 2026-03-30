# DSA 210 Project Proposal
**Student:** Omer  
**Course:** DSA 210 Introduction to Data Science – 2025-2026 Spring Term  
**Submission Date:** March 31, 2026

---

## Project Title
**Social Media Use & Mental Health: A Data-Driven Survey Analysis**

---

## Motivation

Excessive social media use is widely believed to harm mental health, yet the actual quantitative relationship is nuanced and often misrepresented in popular media. Using a real-world survey dataset collected from university students and working adults, I aim to apply rigorous data science methods to determine which social media behaviors are genuinely predictive of poor mental well-being indicators such as anxiety, depression, and distraction — and which are merely incidental.

---

## Data Source & Collection

### Primary Dataset – Social Media & Mental Health Survey
**Source:** Kaggle – [*Social Media and Mental Health*](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health)  
**File:** `smmh.csv` (77 KB)  
This dataset was collected via a real Google Form survey conducted April–May 2022 as part of a university Statistics course project. It contains **481 responses** with the following 21 features:

- **Demographics:** Age, Gender, Relationship Status, Occupation Status, Organization type
- **Usage:** Daily social media time (categorical: Less than 1h → More than 5h), platforms used
- **Mental health indicators (all rated 1–5):**
  - Frequency of purposeless social media use
  - Distraction level when busy
  - Restlessness when not using social media
  - Ease of distraction in general
  - Feeling bothered by worries
  - Difficulty concentrating
  - Frequency of comparing to others
  - Feelings about comparisons
  - Seeking validation from social media
  - Frequency of feeling depressed
  - Fluctuation in interest in daily activities
  - Sleep issues

### Enrichment Dataset – Sleep Health & Lifestyle
**Source:** Kaggle – [*Sleep Health and Lifestyle Dataset*](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)  
This dataset provides **374 records** with complementary well-being signals:
- Sleep duration (hours/night), Sleep quality score (1–10)
- Physical activity level (min/day), Stress level (1–10)
- BMI category, presence of sleep disorders (None, Insomnia, Sleep Apnea)
- Heart rate, daily steps

The two datasets will be enriched by joining on shared demographic attributes (age group, gender, occupation type) to build derived composite mental-health and lifestyle scores for a richer analysis.

**Expected dataset characteristics:**
- **481 primary observations** (smmh.csv), enriched with sleep/lifestyle features
- **21 original features** + ~6 derived/engineered features
- Mixed data types: ordinal (mental health scores 1–5, usage frequency), categorical (platforms, gender, occupation), continuous (age, derived scores)

---

## Planned Analysis

1. **Exploratory Data Analysis (EDA):** Distribution of usage time by platform and demographic group, mental health score distributions, correlation matrix across all ordinal/numeric features, platform-specific emotional profiles.
2. **Hypothesis Testing:**
   - H₁: Higher daily social media usage is associated with higher self-reported distraction and concentration difficulty scores.
   - H₂: Users who frequently compare themselves to others on social media report significantly higher depression/anxiety scores.
   - H₃: Occupation group (students vs. workers) shows a significant difference in social media usage time and its mental health impact.
3. **Machine Learning:**
   - **Classification:** Predict whether a user is at high mental health risk (composite score above median) using Logistic Regression, Random Forest, and Gradient Boosting; compare via cross-validated F1 score.
   - **Regression:** Predict the overall mental health risk score from usage patterns and demographic features.
   - **Feature importance analysis** to identify the strongest predictors of poor mental health outcomes.

---

## Ethical Considerations

Both datasets are fully anonymized public survey datasets published on Kaggle under open licenses. No personally identifiable information is used. All data sources and any AI tools used in the project will be fully documented as required by course policy.

---

## Repository
[https://github.com/omertt27/dsa210-project](https://github.com/omertt27/dsa210-project)
