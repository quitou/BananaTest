import os

def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)

homework_path = os.path.dirname(os.path.dirname(base_path))
alex_gorb_path = os.path.join(homework_path,'Alex_Gorb', 'file.txt')
print(alex_gorb_path)

with open(alex_gorb_path) as gorb_file:
    print(gorb_file.read())