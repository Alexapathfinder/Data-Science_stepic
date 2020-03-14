import pandas as pd
import numpy as np

my_stat = pd.read_csv('my_stat.csv')
print(my_stat.head(10))

# Выполните действие: V5 = V1 + V4

my_stat['V5'] = my_stat['V1'] + my_stat['V4']


# Выполните действие: V6 = натуральный логарифм переменной V2

my_stat['V6'] = np.log(my_stat['V2'])

print(my_stat)

#  Альтернативное решение через assign:

my_stat=my_stat.assign(V5 = my_stat.V1+my_stat.V4, V6 = np.log(my_stat.V2));