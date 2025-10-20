import datetime

# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
date = "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
print(python_date)
# 1. Распечатайте полное название месяца из этой даты
print(python_date.strftime('%B'))
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
print(python_date.strftime('%d.%m.%Y, %H:%M'))

# List comprehension
# Дан такой кусок прайс листа: (Копируйте эту переменную (константу) в код прямо как есть)
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# При помощи генераторов превратите этот текст в словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
convert = list(PRICE_LIST.split())
price = [int(x.replace('р','')) for x in convert[1::2]]
chancellery = [x for x in convert[::2]]
price_dict = dict(zip(chancellery,price))
print(price_dict)
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

