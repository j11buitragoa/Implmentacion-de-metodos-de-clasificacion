# Implementation of Classification Methods
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](#)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#)

This project explores the relationship between **alcohol consumption indices** and **happiness levels** reported across countries.  
We implement and compare **Decision Trees, Logistic Regression, and SVM**, evaluating metrics such as **Accuracy**, **F1**, and **MCC**.  

📄 Associated document: [`docs/Proyecto_final_IA.pdf`](docs/Proyecto_final_IA.pdf)  
🎥 [Video tutorial](https://youtu.be/yvUKA8ZiFak)

---

## 🗂️ Repository Structure
- data/
- raw/
- alcohol_consumption.csv
- world_happiness_2019.csv
- docs/
- notebooks/
- results/
- src/
- train.py
- requirements.txt

---

## 🚀 Installation
# 1.  Create virtual environment 
```bash
python -m venv .venv
```
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```
# 2. Install dependencies
```bash
pip install -r requirements.txt
```
---

## ▶️ Usage
Run the main script:
```bash
python src/train.py
```

## 📊 Features & Expected Results

1. Decision Trees
- Classification on training and test sets.
- Evaluation using MCC and F1 scores.

2. Logistic Regression
- Prediction on the test set.
- Evaluation using Accuracy.

3. SVM
- Classification with Support Vector Machines.
- Evaluation using F1 and MCC.

## 🧠 Datasets

data/raw/alcohol_consumption.csv → Alcohol consumption by country.
data/raw/world_happiness_2019.csv → World Happiness Report 2019 indices.

Both datasets were obtained from [Kaggle](https://www.kaggle.com/).

---

## ✍️ Authors

Juanita Buitrago

Stefan Seigel

---






