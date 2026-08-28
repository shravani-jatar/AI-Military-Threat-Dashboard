
# AI-Based Military Intelligence & Threat Analytics Dashboard

An academic AI and data analytics dashboard for exploring historical terrorism patterns using the Global Terrorism Database (GTD). The application combines interactive visualization, country-level analysis, machine learning-based severity classification, historical risk analysis, forecasting, and automated intelligence summaries in a Streamlit interface.

> **Academic Project:** This system is designed for educational and analytical purposes using historical data. It is not a real-time military command, surveillance, targeting, or operational decision-making system.

---

## Overview

The **AI-Based Military Intelligence & Threat Analytics Dashboard** provides an interactive platform for analyzing historical terrorism incidents and identifying patterns within the data.

The dashboard includes:

* Global historical threat visualization
* Country-level incident analysis
* AI-based historical severity classification
* Historical exposure and risk analysis
* Trend forecasting
* Automated intelligence brief generation
* Interactive data exploration
* Methodology and limitations documentation

The project demonstrates the application of **Python, data analytics, machine learning, and interactive visualization** to a large-scale historical dataset.

---

## Key Features

### 1. Overview Dashboard

Provides a high-level summary of the historical dataset, including incident counts, casualties, geographical distribution, and major trends.

### 2. Global Map

Interactive geographical visualization of historical incidents using latitude and longitude information.

### 3. Country Analysis

Allows users to examine historical terrorism patterns at the country level, including incidents, casualties, attack types, targets, and trends.

### 4. AI Severity Analysis

Uses a machine learning classification model to classify historical incidents into severity categories:

* Low
* Moderate
* High

The model uses incident characteristics available in the dataset.

**Important:** The model classifies the severity of historical incidents. It does not predict the location or timing of future attacks.

### 5. Historical Risk Analysis

Provides an analytical exposure/risk index based on historical incident characteristics and aggregated patterns.

### 6. Forecasting

Analyzes historical trends and provides statistical forecasts based on previously observed data.

Forecasts should be interpreted as analytical estimates rather than predictions of actual future security events.

### 7. Intelligence Brief

Generates an automated summary of selected historical patterns and analytical results.

### 8. Data Explorer

Provides interactive access to the processed dataset and allows users to examine selected variables and records.

### 9. Methodology

Documents the analytical approach, assumptions, limitations, and responsible-use considerations of the system.

---

## Technology Stack

| Component               | Technology                           |
| ----------------------- | ------------------------------------ |
| Programming Language    | Python                               |
| Dashboard Framework     | Streamlit                            |
| Data Processing         | Pandas, NumPy                        |
| Data Visualization      | Plotly                               |
| Machine Learning        | Scikit-learn                         |
| Model Persistence       | Joblib                               |
| Dataset                 | Global Terrorism Database (GTD)      |
| Development Environment | VS Code / Python Virtual Environment |

---

## Project Structure

```text
AI_Military_Threat_Dashboard/
│
├── app.py
├── check_data.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── styles.css
│
├── config/
│   └── settings.py
│
├── data/
│   └── README.txt
│
├── models/
│   └── .gitkeep
│
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Global_Map.py
│   ├── 3_Country_Analysis.py
│   ├── 4_AI_Severity.py
│   ├── 5_Historical_Risk.py
│   ├── 6_Forecasting.py
│   ├── 7_Intelligence_Brief.py
│   ├── 8_Data_Explorer.py
│   └── 9_Methodology.py
│
└── utils/
    ├── analytics.py
    ├── data_loader.py
    ├── forecast.py
    ├── ml.py
    └── risk.py
```

---

# Dataset

This project uses the **Global Terrorism Database (GTD)** provided by the National Consortium for the Study of Terrorism and Responses to Terrorism (START), University of Maryland.

The raw dataset is **not included in this repository** because of its size and applicable dataset licensing/distribution requirements.

### Dataset Required

The application expects the following file:

```text
globalterrorismdb_0718dist.csv.zip
```

### Dataset Location

After downloading or obtaining the dataset, place the ZIP file inside the project's `data` directory:

```text
AI_Military_Threat_Dashboard/
└── data/
    ├── README.txt
    └── globalterrorismdb_0718dist.csv.zip
```

**Do not rename the dataset file**, because the application expects this path:

```text
data/globalterrorismdb_0718dist.csv.zip
```

### Dataset Handling

The application reads the CSV file directly from the ZIP archive. The dataset does **not** need to be manually extracted.

The `data_loader.py` module automatically:

1. Locates the ZIP archive.
2. Identifies the CSV file inside it.
3. Loads the required columns.
4. Performs basic data type conversion.
5. Handles selected missing values.
6. Calculates derived variables such as casualties.
7. Returns the processed dataset to the dashboard.

### Dataset Source

START — National Consortium for the Study of Terrorism and Responses to Terrorism, University of Maryland.

Official GTD information:

https://www.start.umd.edu/gtd

Please follow the applicable GTD end-user license and citation requirements when using the dataset.

---

# Installation and Setup

## Prerequisites

Make sure the following are installed:

* Python 3.10 or later
* Git
* Visual Studio Code

---

## 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/shravani-jatar/AI-Military-Threat-Dashboard.git
```

Move into the project directory:

```bash
cd AI-Military-Threat-Dashboard
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\activate
```

If PowerShell prevents activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.venv\Scripts\activate
```

When the environment is activated, the terminal should display:

```text
(.venv)
```

before the command prompt.

---

## 3. Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

---

## 4. Add the Dataset

Place:

```text
globalterrorismdb_0718dist.csv.zip
```

inside:

```text
data/
```

The final structure should be:

```text
AI-Military-Threat-Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    ├── README.txt
    └── globalterrorismdb_0718dist.csv.zip
```

The application reads the CSV directly from the ZIP archive, so manual extraction is not required.

---

# Running the Application

Make sure the virtual environment is activated.

From the project root directory, run:

```powershell
streamlit run app.py
```

Streamlit will start the local development server.

Open the following address in your browser:

```text
http://localhost:8501
```

If Streamlit provides a different local URL in the terminal, use the URL displayed there.

---

# Optional Model Training

The dashboard can train the machine learning model when the AI Severity module is accessed.

For demonstration purposes, the model can also be trained separately using:

```powershell
python train_model.py
```

The generated model is stored locally in the `models/` directory.

Model files are not required for the basic dashboard startup unless the corresponding functionality requires them.

---

# Application Workflow

```text
Global Terrorism Database
          │
          ▼
     Data Loading
          │
          ▼
   Data Preprocessing
          │
          ├───────────────┐
          ▼               ▼
   Exploratory        Feature
      Analysis       Engineering
          │               │
          │               ▼
          │        Machine Learning
          │               │
          └───────┬───────┘
                  ▼
        Analytics & Forecasting
                  │
                  ▼
        Streamlit Dashboard
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Maps      Analysis     AI
                         Insights
```

---

# Machine Learning

The AI component uses a supervised classification approach to categorize historical incidents into severity classes.

The classification process is based on selected characteristics available within the historical dataset.

The model is intended to demonstrate the application of machine learning to historical incident analysis.

It should not be interpreted as a system capable of predicting future attacks, identifying future targets, or providing operational military intelligence.

---

# Responsible Use and Limitations

This project has been developed as an academic demonstration of data analytics and machine learning.

The system has several important limitations:

* The underlying dataset contains historical information and does not represent real-time events.
* Historical patterns cannot guarantee future outcomes.
* Forecasting results are dependent on the quality and temporal coverage of the available data.
* Machine learning predictions depend on the features and assumptions used during model development.
* The dashboard does not provide real-time threat intelligence.
* The system should not be used for operational targeting, surveillance, military decision-making, or security intervention.
* Dataset licensing and citation requirements must be respected.

---

# Project Objectives

The primary objectives of this project are to:

1. Analyze historical terrorism data using Python-based data analytics.
2. Develop an interactive dashboard for geographical and statistical exploration.
3. Apply machine learning to historical incident severity classification.
4. Develop analytical indicators for historical exposure and risk.
5. Explore temporal trends and forecasting techniques.
6. Present analytical results through an accessible Streamlit interface.
7. Demonstrate responsible and transparent use of AI for historical data analysis.

---

# Running the Project Locally — Quick Reference

After cloning the repository:

```powershell
cd AI-Military-Threat-Dashboard

python -m venv .venv

.venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

Place the dataset at:

```text
data/globalterrorismdb_0718dist.csv.zip
```

Then run:

```powershell
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# Project Status

**Status:** Academic Project / Prototype

The project is intended for demonstration, research, and educational purposes. Future improvements may include enhanced model validation, additional forecasting methods, improved explainability, optimized data processing, and deployment-oriented configuration.

---

# Data Attribution

Global Terrorism Database (GTD), National Consortium for the Study of Terrorism and Responses to Terrorism (START), University of Maryland.

https://www.start.umd.edu/gtd

The dataset is owned and maintained by its respective providers. This project does not claim ownership of the underlying GTD data.

---

# Author

**Shravani**

Student
Savitribai Phule Pune University
