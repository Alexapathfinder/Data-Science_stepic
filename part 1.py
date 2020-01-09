import pandas as pd
import numpy as np
students_performance = pd.read_csv('/home/user/Загрузки/StudentsPerformance.csv')
print(students_performance)
print()
print(students_performance.head())
print()
print(students_performance.tail())
print()
print(students_performance.describe())
print()
print(students_performance.dtypes)
print()
print(students_performance.shape)
print()
print(students_performance.groupby('gender').aggregate({'writing score' : 'mean' }))
print()
print(students_performance.size)
print()
print(students_performance.iloc[0:5, 0:3])
print()
print(students_performance.iloc[0:3, 0:5])
print()
print(students_performance.iloc[[0, 3, 10], [0, 5, -1]])
print()
print(students_performance.iloc[[0, 3, 10], [-1, -2, -3]])
print()
students_performance_with_names = students_performance.iloc[[0, 3, 4, 7, 8]]
print(students_performance_with_names)
print()
students_performance_with_names.index = ["Cersei", "Tywin", "Gregor", "Joffrey", "Ilyn Payne"]
print(students_performance_with_names)
print()
print(students_performance_with_names.loc[["Cersei", "Joffrey"], ['gender', 'writing score']])