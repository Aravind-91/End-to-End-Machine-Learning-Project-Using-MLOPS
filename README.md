# End-to-End-Machine-Learning-Project-Using-MLOPS

---

## Overview
This project focuses on predicting whether a US visa application
will be **Certified** or **Denied** based on applicant and job-related features.

The primary goal of this project is to practice **modular coding**
and understand the structure of an **end-to-end machine learning pipeline**.

---

## Problem Statement
US visa applications go through a certification process based on
multiple factors such as job role, wages, employer details, and location.

The objective of this project is to build a machine learning pipeline
that can learn patterns from historical visa application data and
predict the likelihood of certification.

---

## Dataset
- **Domain:** Immigration / Employment
- **Target Variable:** `case_status`
  - Certified → 1
  - Denied → 0
- **Features include:**
  - Job role
  - Prevailing wage
  - Employer details
  - Work location
  - Case type and other attributes

(Note: Dataset is used for learning and experimentation purposes.)

---

## Approach
The project follows a modular, pipeline-based approach:

1. Data ingestion from source
2. Data validation and basic checks
3. Data preprocessing and feature transformation
4. Model training (baseline model initially)
5. Model evaluation using appropriate metrics
6. DePloyment Using AWS

At the current stage, the focus is on **pipeline structure**
rather than advanced model optimization.

---

## How To Run
```bash
python -m venv usvisa
```

```bash
- source usvisa/Scripts/activate
```

```bash
- pip install -r requirements.txt
```

---

## Workflow:

1. constants
2. entity
3. components
4. pipeline
5. Main file

---

## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```