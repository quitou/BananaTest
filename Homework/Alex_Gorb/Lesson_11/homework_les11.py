# TODO: Задание №1
# Создайте универсальный декоратор, который можно будет применить к любой функции. Декоратор должен делать следующее:
# он должен распечатывать слово "finished"после выполнения декорированной функции.
#
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @finish_me
# def example(text):
#     print(text)
# example('print me')
#
# В результате работы будет такое:
# "print me"
# "finished"
#



def finish_me(func):

    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result
    return wrapper

@finish_me
def example(text):
    print(text)
example('print me')



# Дополнительные задания (необязательные):
# TODO: Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:
##
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=2)
#
# В результате работы будет такое:
# print me
# print me

def repeat_me(func):

    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)
    return wrapper

@repeat_me
def example(text):
    print(text)

example('print me', count=3)

# Задание №3
# Напишите программу:
# Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....

# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def auto_operation(func):

    def wrapper(*args):
        num_1, num_2 = args
        if num_1 < 0 or num_2 < 0:
            return func(num_1, num_2, '+')
        elif num_1 > num_2:
            return func(num_1, num_2, '-')
        elif num_1 < num_2:
            return func(num_1, num_2, '/')
        elif num_1 == num_2:
            return func(num_1, num_2, '*')
        else:
            return 'error'

    return wrapper


@auto_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return 'error'

first_num = float(input('впишите первое число: '))
second_num = float(input('впишите второе число: '))

print(calc(first_num, second_num))