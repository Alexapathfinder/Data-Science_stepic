import pandas as pd
import numbers as np
pd.set_option('display.max_columns', 100)

import matplotlib.pyplot as plt
import seaborn as sns

events_data = pd.read_csv('event_data_train.csv')
submissions_data = pd.read_csv('submissions_data_train.csv')
# print(events_data.head(10))
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')
# print(events_data)
# print(events_data.date.max())
events_data['day'] = events_data.date.dt.date
# print(events_data.head(10))

# print(events_data.groupby('day').user_id.nunique().head())
# events_data.groupby('day').user_id.nunique().plot()
# plt.show()

# print(events_data[events_data.action == 'passed'].groupby('user_id', as_index=False).agg({'step_id': 'count'}) \
#       .rename(columns={'step_id': 'passed_steps'}).head())
#
# events_data[events_data.action == 'passed'].groupby('user_id', as_index=False).agg({'step_id': 'count'}) \
#       .rename(columns={'step_id': 'passed_steps'}).passed_steps.hist()
# plt.show()

# print( events_data[events_data.action == 'passed'].groupby('user_id', as_index=False).agg({'step_id': 'count'}) \
#       .rename(columns={'step_id': 'passed_steps'}).passed_steps.min())
#
# print(events_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0) \
#       .reset_index().head(10))
#
# events_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0) \
#       .reset_index().discovered.hist()
# plt.show()

# print(submissions_data.head())
submissions_data['date'] = pd.to_datetime(submissions_data.timestamp, unit='s')

submissions_data['day'] = submissions_data.date.dt.date

# print(submissions_data.head())

users_scores = submissions_data.pivot_table(index='user_id', columns='submission_status',
                                            values='step_id', aggfunc='count',
                                            fill_value=0).reset_index()
print(users_scores)