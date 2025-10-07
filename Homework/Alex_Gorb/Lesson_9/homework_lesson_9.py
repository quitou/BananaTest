# TODO: Напишите функцию-генератор, которая генерирует список чисел фибоначчи
#  Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

def generator_fibonachi(limit = 100):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield b
        a, b = b, a + b
        count += 1




needed = {5, 200, 1000, 100000}
for i, fib in enumerate(generator_fibonachi(100001), start = 1):
    if i in needed:
        print(f'{i}-e число: {fib}')
    if i == 100000:
        break

fruits = ['яблоко', 'банан', 'апельсин']
for pair in enumerate(fruits):
    print(pair)