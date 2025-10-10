# Map, filter
# Есть такой список:

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.

new_temperatures = list(filter(lambda x: x > 28, temperatures))
print(new_temperatures)

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
max_temp = max(new_temperatures)
min_temp = min(new_temperatures)
middle_temp = round(sum(new_temperatures) / len(new_temperatures), 3)


print(f'Самая высокая температура: {max_temp}, '
      f'Самая низкая температура: {min_temp}, Средняя температура: {middle_temp}')