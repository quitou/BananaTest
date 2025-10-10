from Homework.Alex_Gorb.Lesson_4.python_basics_2 import my_list
import datetime
summer = True

if summer: # вместо if summer is True:
    print('The weather is fine')
else:
    print('The weather is not fine')

a = 0

if a is not None:
    print('...')

numbers = [1, 45, 23, 67, 32, 89]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

a = 1 / 3
print(round(a, 3))

print(abs(-1))

print(sorted(numbers))
print(sorted(numbers, reverse=True))
numbers.sort(reverse=True)
print(numbers)
print('-' * 20)

my_list = [1, 2, 3, 4, 5]

def mult_by(x):
    return x * 2

new_list = map(mult_by, my_list)
print(list(new_list))

# code, number = map(int, input('code and number: ').split())
# print(f'code is {code + 1}, number is {number + 2} ')
print('-' * 20)
new_my_list = [1, 2, 3, 4, 5]

new_my_list_1 = map(lambda x: x * 2, new_my_list)
print(list(new_my_list_1))
print('-' * 20)

my_list = [1, 2, 3, 4 ,5]

def mult_by_2(x):
    if x > 10:
        return x * 5
    else:
        return x * 2

new_list = map(lambda x: x * 5 if x > 10 else x * 2, my_list)
print(list(new_list))

my_list_1 = [1, 2, 3, 5 ,6 ,7]
b = 1 if len(my_list_1) > 4 else 5

print(b)

print('-' * 20)

my_list2 = [1, 2, 3, 4, 5 ,6 ,7, 8]

my_list2_new = []
for x in my_list2:
    if x % 2 == 0 :
        my_list2_new.append(x)
print(my_list2_new)

def is_even(x):
    return x % 2 == 0


new_list2 = filter(is_even, my_list2)
print(list(new_list2))
my_list32 = [1, 2, 3, 4, 5 ,6 ,7, 8]
new_list3 = filter(lambda y: y % 2 == 0, my_list32)
print(list(new_list3))
print('-' * 20)

time_now = datetime.datetime.now()
print(time_now)
print(time_now.hour)
print(time_now.year)
print(time_now.timestamp())

easy_date = datetime.datetime(1970, 1, 15)
print(easy_date.timestamp())

my_time = '2023/06/05 12 hours, 30 mins, 10 secs'

python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')

print(python_date)

human_date = python_date.strftime('Year: %y, month: %B, day: %d')
print(human_date)