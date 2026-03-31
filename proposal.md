# DSA 210 Project Proposal

**Student:** Omer | **Course:** DSA 210 – Spring 2026 | **Date:** March 31, 2026

**Title:** Social Media Use & Mental Health

---

I spend a lot of time on social media and I've noticed it sometimes affects my mood and focus. I want to find out whether this is actually backed by data — do people who use social media more also report higher levels of depression, anxiety, and sleep problems?

**Primary data — Social Media & Mental Health Survey**
([kaggle.com/datasets/souvikahmed071/social-media-and-mental-health](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health))
This is a publicly available dataset on Kaggle. It was collected through a real Google Forms survey conducted in April–May 2022. It has **481 responses** and 21 columns: demographics (age, gender, relationship status, occupation), average daily social media usage time (categorical: less than 1h up to more than 5h), platforms used, and 12 mental health indicators each rated on a 1–5 scale — including distraction, restlessness, difficulty concentrating, depression, anxiety, comparing oneself to others, seeking validation, and sleep issues.

**Enrichment data — Sleep Health & Lifestyle Dataset**
([kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset))
Also publicly available on Kaggle. It contains **374 records** with sleep duration, sleep quality (1–10), stress level (1–10), physical activity (min/day), BMI category, and sleep disorder diagnosis. Since both datasets include age, gender, and occupation type, I will merge representative sleep and stress statistics into the primary survey data by demographic group. This enriches the feature set and lets me examine whether social media usage patterns interact with broader lifestyle and sleep health signals.

The analysis will cover EDA, hypothesis testing (e.g. whether heavy users report worse mental health than light users), and machine learning to predict mental health risk from usage and demographic features.

**Repository:** [github.com/omertt27/dsa210-project](https://github.com/omertt27/dsa210-project)
