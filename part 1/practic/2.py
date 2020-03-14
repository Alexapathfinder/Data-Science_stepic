import pandas as pd

df = pd.read_csv('my_stat.csv')
print(df)

#  В переменную с именем subset_1 сохраните только первые 10 строк и только 1 и 3 колонку:
# subset_1 = df.head(10)
# subset_1 = df[['V1', "V3"]]
# subset_1 = subset_1.head(10)
subset_1 = df[['V1', "V3"]].iloc[:10]
print(subset_1)

# В переменную с именем subset_2 сохраните все строки кроме 1 и 5 и только 2 и 4 колонку:

# subset_2 = df[['V2', "V4"]]
# subset_2 = subset_2.drop([1, 5], axis=0)
# subset_2 = subset_2.reset_index()
# subset_2 = subset_2.drop('index', axis=1)

subset_2 = df[['V2', "V4"]].drop([0, 4], axis=0).reset_index().drop('index', axis=1)
print(subset_2)

# РЕШЕНИЕ №2:
# subset_one = df.iloc[:10, [0, 2]]
# subset_two = df.iloc[:, [1, 3]].drop([0, 4])