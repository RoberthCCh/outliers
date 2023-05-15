import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

# Leer solo las columnas deseadas del archivo csv
# cols = ['Corredor', 'Lugar']
data = pd.read_csv("https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Corredores.csv",
                   index_col=0)

# Calcular la media y la desviación estándar de la columna 'Edad'
media_x = data['Edad'].mean()
std_x = 2*data['Edad'].std()

# Calcular la media y la desviación estándar de la columna 'Tiempo'
media_y = data['Tiempo'].mean()
std_y = 2*data['Tiempo'].std()

# Asignar colores a los puntos en función de si son outliers o no
colors = np.where(abs(data['Edad']-media_x) > std_x, 'red', 'blue')

# Graficar los puntos y los outliers
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Edad'], data['Tiempo'], data['Corredor'], s=20, c=colors)
ax.set_xlabel('Edad')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Corredor')

# Mostrar la gráfica
plt.show()
