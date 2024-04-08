import csv
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Ruta del directorio donde se encuentran los archivos CSV
directorio = r"D:\Documentos\2024-1\Reconocimiento de Patrones\simulated-obstructive-disease-respiratory-pressure-and-flow-1.0.0\PQ_ProcessedData"

# Función para leer el archivo CSV y extraer los valores de la columna 'Pressure [cmH2O]' para los primeros 25 segundos
def leer_presiones(ruta_archivo):
    presiones = []
    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            tiempo = float(fila['Time [s]'])
            if tiempo <= 30:  # Considerar solo los primeros 25 segundos
                presion = float(fila['Pressure [cmH2O]'])
                presiones.append(presion)
            else:
                break  # Salir del bucle si el tiempo excede los 25 segundos
    return presiones

# Lista para almacenar las listas de presiones de cada archivo
lista_presiones = []

# Iterar sobre los archivos en el directorio
for nombre_archivo in os.listdir(directorio):
    if nombre_archivo.endswith(".csv"):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        presiones = leer_presiones(ruta_archivo)
        lista_presiones.append(presiones)

X=lista_presiones
# Definimos los valores de EPOC 
y = ([0] + [200] + [250] + [300])*3*20

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("Listo 1: Variables determinadas")

print(len(X_train))
print(len(y_train))

# Modelo de regresión logística
modeloLR = LogisticRegression()
modeloLR.fit(X_train, y_train)

# Modelo Naive Bayes
modeloNB = GaussianNB()
modeloNB.fit(X_train, y_train)

# Modelo KNN
k = 3
modeloKNN = KNeighborsClassifier(n_neighbors=k)
modeloKNN.fit(X_train, y_train)

print("Listo 2: Modelos entrenados")

# Comprobación de modelos
y_pred_NB = modeloNB.predict(X_test)
y_pred_LR = modeloLR.predict(X_test)
y_pred_KNN = modeloKNN.predict(X_test)

print("Listo 3: Modelos probados")

# Resultados
precision_NB = accuracy_score(y_test, y_pred_NB)
precision_LR = accuracy_score(y_test, y_pred_LR)
precision_KNN = accuracy_score(y_test, y_pred_KNN)

print("Precisión del modelo Naive Bayes:", precision_NB)
print("Precisión del modelo Regresión Logística:", precision_LR)
print("Precisión del modelo KNN:", precision_KNN)