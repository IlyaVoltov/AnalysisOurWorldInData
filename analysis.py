import pandas

#pandas.set_option('display.max_columns', None) # вывести всю таблицу
#pandas.set_option('display.max_rows', None) # вывести всю таблицу

data = pandas.read_csv('Non-stateWarData_v4.0.csv', index_col='WarName')
#unique_data = data['WarType'].unique() # уникальные значения в конкретном столбике

#print(data)
#print(unique_data)

#for column in data:
#    print(column) # возвращает имена колонок в порядке их определения

# поработаем с годами
# определим продолжительность войны
#war_period = data['EndYear'] - data['StartYear']
#print(war_period)

# поработаем со сторонами конфликта (SideA1, SideA2, SideB1, SideB2, SideB3, SideB4, SideB5)

dup_value = data['Initiator']

duplicate_elements = {}

for item in dup_value:                      # Теперь пройдёмся по нашему неупорядоченному списку при помощи цикла for
    if item in duplicate_elements:          # Внутри цикла добавим условие
        duplicate_elements[item] += 1       # если итерабельный элемент присутствует в словаре duplicate_elements, то прибавляем к значению ключа единицу,
    else:
        duplicate_elements[item] = 1        # при else в словарь будет добавляться новый ключ, которого в нём ранее не было

# if duplicate_elements > 1:
#     print(duplicate_elements)

print(duplicate_elements)
