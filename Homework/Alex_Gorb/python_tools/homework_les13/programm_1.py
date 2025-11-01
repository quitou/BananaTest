import os
import datetime



path = os.path.dirname(__file__)
file_path = os.path.join(path,'data.txt')


my_dict = {}
with open(file_path, 'r') as data_file:
    for line in data_file:
        parts = line.strip().split(' ')
        if len(parts) >= 3:
            key = int(parts[0])
        value = f'{parts[1]} {parts[2]}'
        my_dict[key] = value

old_data = datetime.datetime.strptime(my_dict[1], "%Y-%m-%d %H:%M:%S.%f")
new_data = old_data + datetime.timedelta(days=7)
print(new_data)

old_data_2 = datetime.datetime.strptime(my_dict[2], "%Y-%m-%d %H:%M:%S.%f")
print(old_data_2.strftime('%A'))

old_data_3 = datetime.datetime.strptime(my_dict[3], "%Y-%m-%d %H:%M:%S.%f")
print(datetime.datetime.now() - old_data_3)

def input_date(date):
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print('формат неверен, попробуйте ещё раз')

my_date = input('Введите дату')
print(input_date(my_date))
