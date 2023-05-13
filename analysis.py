import pandas

#pandas.set_option('display.max_columns', None) # вывести всю таблицу
#pandas.set_option('display.max_rows', None) # вывести всю таблицу

data = pandas.read_csv('Non-stateWarData_v4.0.csv', index_col='WarName')
#unique_data = data['WarType'].unique() # уникальные значения в конкретном столбике


print(data)
#print(unique_data)