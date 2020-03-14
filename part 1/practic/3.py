import pandas as pd

my_stat = pd.read_csv('my_stat.csv')
print(my_stat.head(10))

# В переменную subset_1 сохраните только те наблюдения, у которых значения переменной V1  строго больше 0,
# и значение переменной V3  равняется 'A'.

subset_1 = my_stat.loc[(my_stat['V1'] > 0) & (my_stat['V3'] == 'A')]
print(subset_1)


# В переменную  subset_2  сохраните только те наблюдения, у которых значения переменной V2  не равняются 10,
# или значения переменной V4 больше или равно 1.

subset_2 = my_stat.loc[(my_stat['V2'] != 10) | (my_stat['V4'] >= 1)]
print(subset_2)


# Как и в предыдущей задаче результат фильтрации - это тоже dataframe.



