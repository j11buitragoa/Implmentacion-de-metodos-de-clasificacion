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
```bash
# 1) Create virtual environment 
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt



## ▶️ Usage
```bash
Run the main script:
python src/train.py

## 📊 Features & Expected Results}

#1) Decision Trees
- Classification on training and test sets.
- Evaluation using MCC and F1 scores.

#2) Logistic Regression
- Prediction on the test set.
- Evaluation using Accuracy.

#3) SVM
- Classification with Support Vector Machines.
- Evaluation using F1 and MCC.

## 🧠 Datasets

 data/raw/alcohol_consumption.csv → Alcohol consumption by country.

data/raw/world_happiness_2019.csv → World Happiness Report 2019 indices.

Both datasets were obtained from [Kaggle](https://www.kaggle.com/).

## ✍️ Authors

Juanita Buitrago

Stefan Seigel

---



<!--
# Implementación de métodos de clasificación

INDICES DE CONSUMO DE ALCOHOL DE CADA PAIS SEGÚN SU REPORTE DE FELICIDAD

Este proyecto tiene como objetivo explorar la relación entre los índices de consumo de alcohol y los niveles de felicidad reportados en diferentes países.
Se realiza mediante la implementación de arboles de decisión, SVM y regresión logistica. Para los datos se hace uso de dos datasets, uno sobre el consumo de alcohol en cada pais y el otro sobre los indices de felicidad en el año 2019.Igualmente se hace la normalización de los datos y la obtención de la precisión del modelo
[Ver video tutorial](https://youtu.be/yvUKA8ZiFak)


## Tabla de contenidos

- [Características](#características)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)


##Características
Implementación de Árboles de Decisión
En esta sección, se utiliza el algoritmo de Árboles de Decisión para clasificar los datos. Se realiza la predicción en los conjuntos de entrenamiento y prueba, y se calculan las puntuaciones de MCC y F1 para evaluar el rendimiento del modelo.

Implementación de Regresión Logística
Aquí se aplica el algoritmo de Regresión Logística para la clasificación. Se realiza la predicción en el conjunto de prueba y se evalúa la precisión del modelo.

Implementación de SVM
Se utiliza el algoritmo SVM (Máquinas de Vectores de Soporte) para la clasificación. Se realiza la predicción en el conjunto de prueba y se calculan la puntuación F1 y el coeficiente de correlación de Matthews (MCC) para evaluar el rendimiento del modelo.

## Requisitos previos

Intalación de librerias en Python e inclusión de los datasets usados

[indice de felicidad](2019.csv),
[consumo de alcohol](drinks.csv)
## Instalación

python clasificacion_IA.py
[code](classification_ia.py) 

-->




