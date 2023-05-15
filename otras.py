import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos de ejemplo
data = pd.read_csv(
    "https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Corredores.csv")

# Seleccionar la variable de interés
variable = 'Edad'

# Calcular media y desviación estándar
media = data[variable].mean()
std = data[variable].std()

# Definir umbral
umbral = 2  # Consideramos como normales los valores dentro de 2 desviaciones estándar

# Detectar outliers
outliers = data[abs(data[variable] - media) > umbral*std][variable]

# Graficar histograma con outliers marcados en rojo
plt.hist(data[variable], bins=20)
plt.xlabel(variable)
plt.ylabel('Frecuencia')
plt.axvline(media, color='k', linestyle='--')
plt.axvline(media-umbral*std, color='r', linestyle='--')
plt.axvline(media+umbral*std, color='r', linestyle='--')
plt.scatter(outliers, [0]*len(outliers), color='r', marker='x', s=100)
plt.show()

# Generar boxplot
green_diamond = dict(markerfacecolor='g', marker='D')
fig, ax = plt.subplots()
ax.set_title('Boxplot por Edades')
ax.boxplot(data[variable], flierprops=green_diamond, labels=["Edad"])
plt.show()
