'''
Пришло время узнать, кто самый главный рак какая роль в dota самая распространённая.
Скачайте датасэт с данными о героях из игры dota 2 и посмотрите на распределение их возможных ролей
в игре (колонка roles). Постройте гистограмму, отражающую скольким героям сколько ролей приписывается
(по мнению Valve, конечно) и напишите какое число ролей у большинства героев.
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dota_hero_stats.csv')
# print(df)
#
# lenths = [len(r.split(',')) for r in df.roles]
# df['lenths'] = lenths
# print(df['lenths'].mean())
# print(df.roles.str.split(',').apply(len).mode())
# sns.distplot([x.count(',')+1 for x in df.roles], bins=15)
# plt.show()
df['number_of_roles'] = df.roles.str.count(',') + 1

df.number_of_roles.hist()
plt.show()
print(df)
