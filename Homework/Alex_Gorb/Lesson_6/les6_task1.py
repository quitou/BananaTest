# Задание 1
# Дан такой список:
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
name, last_name, city, phone, country = person
print(f'Имя: {name}, Фамилия: {last_name}, Город: {city}, Номер телефона: {phone}, Страна: {country}')
# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
string1 = "результат операции: 42"
string2 = "результат работы программы: 547"
string3 = "результат: 5"
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

# TODO: String #1
separator = string1.index(':')
number_one = int(string1[separator + 1:].strip()) + 10
print(number_one)
separator = string2.index(':')
number_two = int(string2[separator + 1:].strip()) + 10
print(number_two)
separator = string3.index(':')
number_three = int(string3[separator + 1:].strip()) + 10
print(number_three)



# Задание 3
# Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

print('Students', ', '.join(students),'study these subjects:', ', '.join(subjects))