
test = "test"
test += ' new'
print(test)
print('-' * 15)
print('Copyrights')
print('-' * 15)

text = 'I love Python'
print('love' in text)
print('-' * 15)

b = 3
print(id(b))
c = 3
print(id(c))
print(b is c)
d = 257673419
print(id(d))
f = 257673419
print(id(f))
print(d is f)
print('-' * 15)

#name = str(input('What is your name ?'))
#print('Привет, ' + name)
#print('-' * 15)

#user_input = input('Enter number')
#print(type(user_input))

a ='1'
print(type(a))
a = int(a)
print(type(a))
print('-' * 15)

my_list = [1,6,15,2, None, 'text', False, 2.42, 'last']
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[-3])

my_list[2] = 42
print(my_list)

my_list1 = []
my_list = list()
print(my_list)
my_list1.append(42)
my_list1.append('text')
print(my_list1)
print(len(my_list1))
print(my_list1.index('text'))
popped = my_list1.pop(0)
print(my_list1)
print(popped)
print('text' in my_list1)
print('-' * 15)

my_tuple = (1,6,15,2, None, 'text', False, 2.42, 'last', 2, 'text')
print(my_tuple[2])
print(my_tuple[-2])
# my_tuple[4] = 42 - вызовет ошибку
print(my_tuple.count(2))
print(my_tuple.index(2.42))

llist = [56]
print(llist)
ttuple = (56,)
print(ttuple)

my_set = {1, 3, 6 ,7, None, 'text', False, 2.42, 3, 7}
# print(my_set[2]) не выведет 2 элемент
print(my_set)
my_set.add(42)
my_set.add('text')
print(my_set)
print('-' * 15)

list2 = [1, 2, 5 ,6 ,2, 1, 8]
list2 = set(list2)
print(list2)
list2 = list(list2)
print(type(list2))
list3 = list({1, 2, 5, 6, 2, 1, 8, 5})
print(list3, type(list3))

test_set = {} # Это создается словарь
print(type(test_set))
my_set_1 = set() # множество (set) - можно создать только так
print(type(my_set_1))
print('-' * 15)

my_dict = {'one': 42, 'two': 56}
print(my_dict)
print(my_dict['one'])
print(len(my_dict))
my_dict['one'] = 666
my_dict['three'] = 90
my_dict['four'] = False
my_dict['five'] = [1, 5 ,8]
my_dict['six'] = {1, 6 ,9}
my_dict[2] = '1231'
my_dict[2.42] = 'dasda'
my_dict[(1, 2)] = 'wqeqdq'
my_dict[5] = {1:2}
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) # все ключи и значения словаря