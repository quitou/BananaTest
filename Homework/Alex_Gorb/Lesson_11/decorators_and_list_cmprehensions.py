


def calc():
    print(1+ 1)

calc()
print(calc)
new_calc = calc
print(new_calc)
new_calc()

def greet():

    def hello():
        return 'hello'
    return hello()

print(greet())

def outer():

    def inner():
        result = 2 + 5
        return result
    return inner
print(outer()())

print('-' * 29)

def func1(give_me_a_func):
    print('before')
    give_me_a_func()
    print('after')

def simple1():
    print('simple1')

def simple2():
    print('simple2')

    func1(simple2)
    func1(simple1)

print('-' * 29)

def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@add_text
def simple3():
    print('simple3')

@add_text
def simple4():
    print('simple4')

simple3()

print('-' * 29)

def add_logs(func):

    def wrapper():
        print(f'function {func.__name__} started')

    return wrapper

@add_logs
def simple5():
    print('simple5')

simple5()

print('-' * 29)

def add_logs1(func):

    def wrapper(*args):
        print(f'function {func.__name__} started')
        result = func(*args)
        return result

    return wrapper

@add_logs1
def calc(x):
    print(x * 2)

@add_logs1
def calc2(x, y):
    print(x * y)

calc(3)
calc2(2, 4)
print('-' * 29)

my_list = [1, 4, 10, 66, 1234, 5, 10]

new_list = [x * 2 for x in my_list]

print(new_list)

new_list1 = [x for x in my_list if x % 2 == 0]
print(new_list1)
print('-' * 29)

data = [('one', 1), ('two', 2)]

# new_dict = {key: value for key, value in data}
new_dict = dict(data)

print(new_dict)

countries = ['USA', 'Hawaii', 'Cuba', 'qwer']
temps = [23, 33, 35, -1]

print(dict(zip(countries, temps)))