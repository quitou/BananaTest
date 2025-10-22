import json

# def read_file(filename):
#     file_data = open(filename, 'r')
#     # data = file_data.read()
#     data = json.load(file_data)
#     file_data.close()
#     return data

# data1 = read_file('data1.txt')
# data2 = read_file('data2.txt')

# print(data1['Country'])
# print(data2['Country'])

print('-' * 20)

class CountryData:

    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']

    @property
    def data(self):
        return self.__data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self.__is_comfort()

    @avg_temp.setter
    def avg_temp(self, value):
        self.__avg_temp = value


    def __read_file(self):
        file_data = open(self.__filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def __is_comfort(self):
        return self.__avg_temp > 25

    def __str__(self):
        return f'File{self.__filename} with data {self.__data}'

    def __repr__(self):
        return f'File {self.__filename} with data {self.__data}'

    def __lt__(self, obj):
        return self.__avg_temp < obj.avg_temp

    def __le__(self, obj):
        return self.__avg_temp <= obj.avg_temp

    def __add__(self, other):
        return self.__avg_temp + other.avg_temp

data1 = CountryData('data1.txt')
print(data1.data)
#print(data1.avg_temp)
print(data1.comfort)

class CountryDataWithMinTemp(CountryData):
    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']

data3 = CountryDataWithMinTemp('data3.txt')
print(data3.min_temp)
print(data3.avg_temp)
print(data1.avg_temp)
print(data1)
print(data1 < data3)
print(data1 + data3)