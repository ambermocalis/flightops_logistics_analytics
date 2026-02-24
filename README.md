# Airline On-Time Performance Analytics ✈️  
#### **End-to-End Data, Machine Learning, and Business Intelligence Project**

![License](https://img.shields.io/badge/License-AGPL--3.0-orange.svg) ![Repository status](https://img.shields.io/badge/Status-In%20Development-yellow.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/ambermocalis/flightops_logistics_analytics) 
![Python version](https://img.shields.io/badge/Python-3.11-blue.svg) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green.svg) ![SQL](https://img.shields.io/badge/SQL-SQLite/Postgres-lightgray.svg)

## Summary
This project analyzes U.S. airline on-time performance using data from the Bureau of Transportation Statistics (BTS) to identify delay drivers and predict whether a flight will arrive 15+ minutes late.

It demonstrates:
- Relational database design using PostgreSQL
- Data cleaning and feature engineering in Python
- Interpretable machine learning models
- Business-focused Power BI dashboards

---

## Business Problem
Flight delays are costly for airlines and disruptive for passengers.  
The objectives of this project are to:

1. Identify operational factors associated with late arrivals  
2. Predict high-risk flights using historical data  
3. Translate analytical insights into actionable, visual outputs  

---

## Dataset
- **Source:** U.S. Bureau of Transportation Statistics (BTS)  
- **Scope:** 24 months of domestic U.S. flights  
- **Target variable:** `ArrDel15` (arrival delay ≥ 15 minutes)  

---

## Technical Approach

### Data Architecture
- **Database:** PostgreSQL  
- **Schema:** Star schema optimized for analytics and BI tools  

**Fact Table**
- One row per flight

**Dimension Tables**
- Date  
- Carrier  
- Airport  

---

### Modeling
Two supervised classification models were trained and compared:

| Model | Purpose | Key Strength |
|------|--------|-------------|
| Logistic Regression | Baseline | Interpretability |
| Gradient Boosting | Final model | Higher predictive performance |

**Evaluation metrics**
- ROC-AUC  
- Precision and Recall  
- Feature importance via permutation testing  

---

(Draft hypotheses, provide insights after modeling is complete)
## Key Insights 
- Delay likelihood varies significantly by **time of day** and **origin airport**
- Certain carriers consistently outperform peers after controlling for route and timing
- Tree-based models capture non-linear delay patterns better than linear baselines

---

## Business Recommendations
- Prioritize operational buffers during high-risk time windows
- Focus delay mitigation efforts on consistently underperforming airports
- Use predictive risk buckets to support proactive scheduling decisions

---

## Power BI Dashboard
The Power BI report includes:

1. Executive on-time performance overview  
2. Delay driver analysis  
3. Predictive delay risk segmentation  

📊 Screenshots will be available in `/powerbi/screenshots`

---

## Tools & Skills Demonstrated
- Python (pandas, scikit-learn)
- PostgreSQL and SQL
- Dimensional data modeling
- Machine learning model evaluation
- Power BI data storytelling

---

## How to Reproduce
1. Load BTS data into PostgreSQL using the provided SQL and Python scripts  
2. Run notebooks in sequence (`01_extract_load` → `05_modeling`)  
3. Connect Power BI directly to the PostgreSQL database  
