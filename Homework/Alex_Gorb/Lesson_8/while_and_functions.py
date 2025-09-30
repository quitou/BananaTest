i = 0

while i < 5:
    print('hello')
    i += 1

print('-' * 20)

# while True:
#     user_input = input('Enter somthing: ')
#     if user_input == 'exit':
#         break
#     elif user_input == '1':
#         print('skiping....')
#         continue
#     elif len(user_input) > 10:
#         print('Your input is too long')
#     else:
#         print('input is ok')
# print('good bye')

text = 'Sed vitae justo malesuada, commodo libero eu end , bibendum mauris.'

words = text.split()
fin_words = []
for word in words:
    if word == 'end':
        break
    elif 'o' in word:
        print(word)
        continue
    fin_words.append(word)

print(' '.join(fin_words))

print('-' * 20)

a = 1
b = 5
c = 4
d = 7
y = 5

main_number = 47

print(a + main_number)
print(b + main_number)
print(c + main_number)
print(d + main_number)
print(y + main_number)

print('-' * 20)

a = 1
b = 5
c = 4
d = 7
y = 5

main_number = 47

def calc(num):
    print(num + main_number)


calc(a)
calc(b)
calc(c)
calc(d)
calc(y)

print('-' * 20)

a = 1
b = 5
c = 4
d = 7
y = 0



def calc(num):
    if num == 0:
        print(num)
    else:
        print(num + main_number)


calc(a)
calc(b)
calc(c)
calc(d)
calc(y)

print('-' * 20)

a = 1
b = 5
c = 4
d = 7
y = 0

def calc(num):
    if num == 0:
        return num
    else:
        return num + main_number

print(calc(a))
result = calc(b)
print(result)
calc(c)
calc(d)
calc(y)

print('-' * 20)

def print_words(first, second, third, fourth, fifth):
    print(f'The first word is {first}, second word is {second}, {third}, {fourth}, {fifth}')

print_words('one', 'two', 'three', 'four', 'five')
print_words(fifth='five', third='three', fourth='four', first='one', second='two')

print('-' * 20)

def power(number, degree=2):
    return number ** degree

print(power(4,3))

print('-' * 20)

def example(e, f, g, ff='one', gg = 'gg'):
    print(e, f, g, ff, gg)

example(2, 3, 4, gg = '444')

print('-' * 20)

def esst(*args):
   # print(args)
   #  result = 0
   #  for x in args:
   #      result += x
   #  return result
   return sum(args)

print(esst(1, 4, 6))

print('-' * 20)

def price_list(**kwargs):
    for  title, price in kwargs.items():
        print(f'Product {title} price is {price}')

price_list(iphon = 2500, laptop = 1, samsung = 4)

