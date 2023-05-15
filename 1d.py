import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
rios = pd.read_csv("https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Rios.csv",
                   engine='python', index_col=0)
rios_unique, counts = np.unique(rios, return_counts=True)

sizes = counts*100
colors = ['blue']*len(rios_unique)
colors[-1] = 'red'

plt.axhline(1, color='k', linestyle='--')
plt.scatter(rios_unique, np.ones(len(rios_unique)), s=sizes, color=colors)
plt.yticks([])
plt.show()
