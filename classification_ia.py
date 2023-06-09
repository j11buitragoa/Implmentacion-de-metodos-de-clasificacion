

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import matthews_corrcoef, f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

"""##Preprocesamiento"""

happiness_data = pd.read_csv('2019.csv',delimiter=',',decimal='.')
drink_data = pd.read_csv('drinks.csv',delimiter=',',decimal='.')
combined_data = happiness_data.merge(drink_data, on='Country')
target=combined_data['Country']
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(combined_data[['Overall rank','Score','GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption','beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']])
pca = PCA(n_components=2)  
pca.fit(normalized_data)
transformed_data = pca.transform(normalized_data)
#plt.scatter(transformed_data[:, 0], transformed_data[:, 1])
#plt.xlabel('Componente Principal 1')
#plt.ylabel('Componente Principal 2')
#plt.title('PCA')
#plt.show()
# Selección de características relevantes
features = combined_data[['Score', 'total_litres_of_pure_alcohol']]
# Definición de la columna 'AlcoholCategory' basada en el consumo de alcohol puro
combined_data['AlcoholCategory'] = 'Bajo'  # Inicialmente, establecer todas las categorías como 'Bajo'
# Definición del umbral para la categoría 'Alto'
umbral_alto = 6.0
# Actualización de la categoría a 'Alto' para los países con consumo de alcohol superior al umbral
combined_data.loc[combined_data['total_litres_of_pure_alcohol'] > umbral_alto, 'AlcoholCategory'] = 'Alto'

X_train, X_test, y_train, y_test = train_test_split(normalized_data, target, test_size=0.2, random_state=42)

X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

"""##Implmentación Arboles de decisión"""

decision_tree = DecisionTreeClassifier()
decision_tree.fit(normalized_data, target)
countries_high_alcohol = decision_tree.predict(normalized_data)
# Realizar predicciones en los conjuntos de entrenamiento y prueba
train_predictions = decision_tree.predict(X_train_normalized)
test_predictions = decision_tree.predict(X_test_normalized)

# Calcular la puntuación de MCC en los conjuntos de entrenamiento y prueba
train_mcc = matthews_corrcoef(y_train, train_predictions)
test_mcc = matthews_corrcoef(y_test, test_predictions)

# Calcular la puntuación F1 en los conjuntos de entrenamiento y prueba
train_f1 = f1_score(y_train, train_predictions, average='weighted')
test_f1 = f1_score(y_test, test_predictions, average='weighted')

# Imprimir los resultados
print('Puntuación de MCC (conjunto de entrenamiento):', train_mcc)
print('Puntuación de MCC (conjunto de prueba):', test_mcc)
print('Puntuación F1 (conjunto de entrenamiento):', train_f1)
print('Puntuación F1 (conjunto de prueba):', test_f1)

# Obtención del índice del país con mayor consumo de alcohol
country_index = combined_data['total_litres_of_pure_alcohol'].argmax()

# Obtención del país más feliz
country_happiest = combined_data.loc[country_index, 'Country']


alcohol_consumption = combined_data.loc[country_index, 'total_litres_of_pure_alcohol']

# Imprimir el país más feliz y el nivel de consumo de alcohol
print("País más feliz:", country_happiest)
print("Consumo de alcohol:", alcohol_consumption)


# Crear un nuevo DataFrame con el país, felicidad y consumo de alcohol
result_df = combined_data[['Country', 'total_litres_of_pure_alcohol','Overall rank','Score','GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption','beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']]

# Ordenar el DataFrame por felicidad de forma descendente
result_df = result_df.sort_values(by='Score', ascending=False)


# Configurar opciones de visualización
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
pd.set_option('display.width', 120)  # Ajustar el ancho de la salida

# Imprimir la tabla fusionada 
print(combined_data.to_string(index=False))

"""##Implementación de regresión logística"""

labels = combined_data['AlcoholCategory']  # Etiqueta  función del consumo de alcohol
# División del conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Creación y entrenamiento del modelo de Regresión Logística
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Predicción de las etiquetas para el conjunto de prueba
y_pred = logreg.predict(X_test)

# Impresión de los resultados de la clasificación
print("Predicciones:")
for country, prediction in zip(X_test.index, y_pred):
    happiness_score = combined_data.loc[country]['Score']
    print("País:", combined_data.loc[country]['Country'], "- Puntuación de felicidad:", happiness_score, "- Categoría de consumo de alcohol:", prediction)

# Evaluación del rendimiento del modelo
accuracy = logreg.score(X_test, y_test)
print("\nPrecisión del modelo:", accuracy)

"""##Implementación de SVM"""

labels = combined_data['AlcoholCategory']  # Etiqueta  función del consumo de alcohol

# Mapeo de las etiquetas "Alto" y "Bajo" a valores numéricos (0 y 1)
labels = labels.map({'Bajo': 0, 'Alto': 1})

# División del conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Creación y entrenamiento del modelo SVM
svm = SVC()
svm.fit(X_train, y_train)

# Predicción de las etiquetas para el conjunto de prueba
y_pred = svm.predict(X_test)

# Cálculo de la puntuación F1
f1 = f1_score(y_test, y_pred)

# Cálculo del coeficiente de correlación de Matthews (MCC)
mcc = matthews_corrcoef(y_test, y_pred)

# Impresión de los resultados de la clasificación
print("Predicciones:")
for country, prediction in zip(X_test.index, y_pred):
    happiness_score = combined_data.loc[country]['Score']
    print("País:", combined_data.loc[country]['Country'], "- Puntuación de felicidad:", happiness_score, "- Categoría de consumo de alcohol(asumiendo que 1 es alto y 0 es bajo):", prediction)

# Evaluación del rendimiento del modelo
accuracy = svm.score(X_test, y_test)
print("\nPrecisión del modelo:", accuracy)
print("Puntuación F1:", f1)
print("Coeficiente de correlación de Matthews (MCC):", mcc)
