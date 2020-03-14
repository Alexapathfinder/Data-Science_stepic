import pandas as pd


my_stat = pd.read_csv('my_stat_1.csv')

my_stat.columns = ['session_value', 'group', 'time', 'n_users']
print(my_stat)

# Для данных my_stat рассчитайте среднее значение переменной session_value для каждой группы (переменная group),
# в получившемся dataframe переменная group не должна превратиться в индекс.
# Также переименуйте колонку со средним значением session_value в mean_session_value.

mean_session_value_data = my_stat.groupby('group')['session_value'].mean()
mean_session_value_data = mean_session_value_data.reset_index()
mean_session_value_data.columns = ['group', 'mean_session_value']
print(mean_session_value_data)

# Альтернатива:

mean_session_value_data = my_stat.groupby("group", as_index=False).session_value.agg({'mean_session_value':'mean'})