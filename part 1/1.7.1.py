import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('income.csv')
print(df)
sns.lineplot(x=df.index, y=df.income)
df.plot()
df['income'].plot()
df.plot(kind='line')
df.income.plot()
sns.lineplot(data=df)
plt.plot(df.index, df.income)
plt.show()