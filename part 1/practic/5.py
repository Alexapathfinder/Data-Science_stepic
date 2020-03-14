import pandas as pd


my_stat = pd.read_csv('my_stat.csv')

my_stat.columns = ['session_value', 'group', 'time', 'n_users']
print(my_stat.head(10))