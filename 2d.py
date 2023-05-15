import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer solo las columnas deseadas del archivo csv
# cols = ['Corredor', 'Lugar']
data = pd.read_csv("https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Corredores.csv",
                   index_col=0)

# Calcular la media y la desviación estándar de la columna 'Corredor'
media = data['Edad'].mean()
std_x = 2*data['Edad'].std()

# Calcular la media y la desviación estándar de la columna 'Lugar'
media_y = data['Tiempo'].mean()
std_y = 2*data['Tiempo'].std()

# Asignar colores a los puntos en función de si son outliers o no
colors = ['blue'] * len(data)
for index, x in enumerate(data['Edad']):
    if abs(x - media) > std_x:
        colors[index] = 'red'

# Graficar los puntos y los outliers
plt.scatter(data['Tiempo'], data['Edad'], s=100, color=colors)
plt.axhline(media, color='k', linestyle='--')
plt.axvline(media_y, color='k', linestyle='--')

# Graficar el elipse que encierra los puntos no outliers
v = media   # y-position of the center
u = media_y  # x-position of the center
b = std_x   # radius on the y-axis
a = std_y  # radius on the x-axis
t = np.linspace(0, 2*np.pi, 100)
plt.plot(u + a*np.cos(t), v + b*np.sin(t))

# Establecer etiquetas de los ejes
plt.xlabel('Tiempo')
plt.ylabel('Edad')

# Mostrar la gráfica
plt.show()
