import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('genome_matrix.csv')
print(df)
data = df.drop(df.columns[0], axis='columns')
print(data)
g = sns.heatmap(data, center=0, cmap='viridis')
g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)
plt.show()
