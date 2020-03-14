import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_csv('iris.csv')
# # df = df.drop(df.columns[[0]], axis='columns')
# df = df.drop(['Unnamed: 0', 'species'], axis=1)
# print(df)
# # # for column in df:
# # #       ax = sns.distplot(df[column])
# # # #       plt.show()
# # for column in df:
# #     sns.kdeplot(df[str(column)])
# # plt.show()
# # # sns.distplot(df['sepal length'])
# # # plt.show()
# colors = ['g', 'r', 'blue', 'yellow', 'white']
# # for col, color in zip(df.iloc[:, :-1], colors):
# #     sns.distplot(df[col], kde_kws = {'color':color, 'lw':1, 'label':col})
# # plt.show()
# # sns.set(style="whitegrid")
# # ax = sns.violinplot(x=df["petal length"], orient='v', color = 'purple')
# # plt.show()
# sns.set(style="ticks", color_codes=True)
# g = sns.pairplot(df)
# plt.show()
# print(df.corr())

iris = pd.read_csv('iris.csv', index_col=0)
sns.pairplot(iris, vars=iris.columns[:4], hue="species")
plt.show()