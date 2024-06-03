# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = (['Каждый','охотник'], 3, 4, True)
print("Незменяемый объект 'Кортеж':", immutable_var)    #   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
print(type(immutable_var))  # immutable_var - это кортеж
#  попытка изменить элемент кортежа, например:
#       immutable_var[2] = 8
#  выдаст ошибку, т.к кортеж не поддерживает обращение по элементам.
print('Кортеж (tuple) не поддерживает обращение по элементам\n')
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = ['желает', 'знать', 7, 8, False]
print("Изменяемый объект 'Список':", mutable_list)
print(type(mutable_list))
#   - Измените элементы списка mutable_list.
mutable_list[0]='умеет'
mutable_list[1]='стрелять'
mutable_list[4]='NULL'
#   - Выведите на экран измененный список mutable_list.
print("Измененный Список:", mutable_list)