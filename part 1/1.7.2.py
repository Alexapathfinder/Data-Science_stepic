import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("dataset_209770_6.txt", sep=" ")
print(df)
# plt.figure()
# sns.stripplot(data=df)
# plt.show()
sns.lmplot(x='x', y='y', data=df)
plt.show()
sns.scatterplot(df.iloc[:, 0], df.iloc[:, 1])
plt.show()