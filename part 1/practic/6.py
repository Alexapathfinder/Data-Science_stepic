import pandas as pd


my_stat = pd.read_csv('my_stat_1.csv')

my_stat.columns = ['session_value', 'group', 'time', 'n_users']
# print(my_stat)

# В переменной session_value замените все пропущенные значения на нули.

# print(my_stat['session_value'].isna().sum())
my_stat['session_value'] = my_stat['session_value'].fillna(0)
# print(my_stat)

# В переменной n_users замените все отрицательные значения на медианное значение переменной n_users
# (без учета отрицательных значений, разумеется).

# n_users_more_null = my_stat[my_stat['n_users'] > 0]
# median = n_users_more_null['n_users'].median()

median = my_stat[my_stat['n_users'] > 0].n_users.median()
my_stat.loc[my_stat['n_users'] < 0, 'n_users'] = median


#  Альтернативное решение второго вопроса:

my_stat.loc[my_stat.n_users<0, 'n_users'] = my_stat.query("n_users>=0").n_users.median()

print(my_stat)

