# ✈️ FlightOps: U.S. Flight Delay Prediction & Operational Performance Dashboard

### Logistics analytics with machine learning, SQL, and BI dashboards

![Python version](https://img.shields.io/badge/Python-3.11-blue.svg) ![License](https://img.shields.io/badge/License-AGPL--3.0-orange.svg) ![Repository status](https://img.shields.io/badge/Status-In%20Development-yellow.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/ambermocalis/flightops_logistics_analytics) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green.svg) ![SQL](https://img.shields.io/badge/SQL-SQLite/Postgres-lightgray.svg)

FlightOps is a logistics analytics project that models U.S. flight arrival delays and builds an operational KPI dashboard using publicly available data from the Bureau of Transportation Statistics (BTS).  

This project demonstrates two core analytics capabilities:

1. **Predictive Modeling (Python)** – A machine learning model that predicts whether a flight will arrive 15+ minutes late using historical on-time performance data.

2. **Operational Intelligence (SQL + BI)** – A relational database and interactive dashboard that provide KPIs such as on-time rates, average delay minutes, cancellation trends, carrier performance, and route-level delay behavior.

This combined workflow reflects analytical tasks similar to those used in transportation logistics, mobility operations, and mission readiness analysis in DoD and federal environments.

---

## 📊 Project Components

### **1. Data Acquisition**
Flight data for 2018–2019 is sourced from the BTS TranStats repository using an automated downloader script:

- `download_bts_ontime.py` fetches monthly On-Time Performance files and extracts them into the project directory.

### **2. Python Modeling**
- Data cleaning and preprocessing  
- Feature engineering (temporal features, route-level features, categorical encoding)  
- Training and evaluation of classification models (Logistic Regression, Tree-based models)  
- Interpretation and performance reporting  
- Exportable notebook for transparency and reproducibility  

> Output: A model that predicts `ARR_DEL15` (arrival delay ≥ 15 minutes).

### **3. SQL Data Pipeline**
- Structured relational database (e.g., SQLite/Postgres)  
- Tables for `Flights`, `Airports`, and `Carriers`  
- Analytical SQL queries supporting dashboard KPIs  
- Queries designed for operational monitoring and trend analysis  

### **4. Dashboard (Power BI or Tableau)**
The dashboard visualizes:
- Overall on-time performance  
- Delay trends by month, carrier, and airport  
- Worst-performing routes  
- Cancellation/diversion behavior  
- Flight throughput metrics  

---
## Insights from work in progress
#### Model Comparison & Recommendation
A logistic regression model was used as an interpretable baseline to estimate arrival delay risk. A gradient boosting classifier was then trained on the same feature set to capture nonlinear and interaction effects.

The gradient boosting model achieved a modest improvement in ROC AUC (0.634 vs 0.617), indicating better ranking of high-risk flights. However, the improvement was incremental rather than dramatic, reflecting the inherently noisy nature of airline delay data and the limited feature set used.

Given this tradeoff, logistic regression is recommended for policy analysis and stakeholder communication due to its interpretability, while gradient boosting is better suited for operational risk scoring where marginal performance gains translate to meaningful improvements at scale.

---

## 📁 Repository Structure

(Initial structure — will grow as the project evolves.)
```
flightops_logistics_analytics/
.
│
├── dashboard/
│ └── # Power BI / Tableau files 
│
├── data/
│ └── raw/  # Auto-populated by downloader script (ignored by Git)
|    └──csv/
│
├── docs/
│ ├── data_dictionary.md
│ ├── erd.png
│ └── dashboard_screenshots/
│
├── notebooks/ # Python notebooks for EDA + modeling
│ ├── 01_flight_delay_predictions.ipynb
│ └── download_bts_ontime.py # Automated BTS monthly downloader
│
├── sql/
│ ├── create_tables.sql
│ ├── load_data.sql
│ └── analytics_queries.sql
│
├── environment.lock.yml # Conda environment file (ignored by Git)
├── environment.yml # Conda environment file
├── LICENSE
└── README.md
```

---

## ❗ Why the `data/` Folder Is Excluded from GitHub

This project uses **large public datasets** from the BTS TranStats On-Time Performance database. Individual monthly CSVs can range from 50MB to 500MB, and including them in version control would:

- Inflate the repository size  
- Slow down cloning and Git operations  
- Risk committing raw data that can be reconstructed programmatically  

Instead, the repository includes:

- **Downloader scripts** to obtain the data  
- **Processing code** for cleaning and modeling  
- **Environment files** to reproduce the analysis  
- **Documentation** describing the schema and workflow  

This approach is standard practice in data science and ensures the repo stays maintainable and professional.

---

## 🛠 Setup Instructions

### **1. Create the Conda environment**

Dependencies are managed with Conda using a curated environment.yml to ensure portability across macOS (Apple Silicon), Linux, and CI environments.

```bash
conda env create -f environment.yml
```
```bash
conda activate datasci311
```
**2. Download the BTS data**

From the repo root:
```bash
python notebooks/download_bts_ontime.py
```

This populates:

data/raw/    
data/raw/csv/

**3. Run notebooks**

Open `01_flight_delay_predictions` in notebooks/ to explore EDA, feature engineering, and model training.

## 📚 Data Source

U.S. Department of Transportation
Bureau of Transportation Statistics (BTS)
**On-Time Reporting Carrier On-Time Performance (1987–Present)**
[https://transtats.bts.gov/](https://transtats.bts.gov/)

## 🚀 Status

📌 In development:
- Data documentation
- Python model notebook
- SQL schema and queries
- Dashboard prototype

## 📄 License

This project is licensed under the AGPL-3.0 License.
See the LICENSE file for details.

## 🙌 Contact

Created by Amber Mocalis
For questions or collaboration opportunities, I would love to connect via [LinkedIn](https://www.linkedin.com/in/ambermocalis).
