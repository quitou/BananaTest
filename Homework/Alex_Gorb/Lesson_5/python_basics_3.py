my_list = [1, 3]
my_tuple = (3, 6 ,9)
# a = my_list[0]
# b = my_list[1]
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]
a, b = my_list
c, d, e = my_tuple
print(a, b, c, d, e)

new_list = [1, 3, 5 ,2 ,15, 7 ,99, 3, 1 ,4]
print(new_list)
print(new_list[0:4])
print(new_list[:4])
print(new_list[3:])
print(new_list[1::2])
print(new_list[::3])
print(new_list[::-1])
print(new_list[-2:-5:-1])
print('-' * 20)

text = 'some text maybe long maybe not'
print(text[3])
print(len(text))
print(text.index('text'))
print(text.count('long'))
#print(text.find('long'))
print(text[:7])
print('maybe' in text)
print(text.startswith('some'))
print(text.endswith('some'))
print('-' * 20)

txt = 'ThIs tExT wITh meSSed'
print(txt.capitalize())
print(txt.title())
print(txt.upper())
print(txt.lower())
print('-' * 20)

some_text = 'some text  maybe long'
string_index = text.index('maybe')
print(some_text[:string_index].lower() + some_text[string_index:].upper())
print('-' * 20)

msg = 'Hellow World'
msg = msg.replace('World', 'Universe')
print(msg)
print('-' * 20)

first_text = ' phone '
first_text = first_text.strip()
first_text = first_text.lstrip()
first_text = first_text.rstrip()
print(first_text)
print('-' * 20)

my_string = 'some little text'
my_string_2 = 'some,little,text'
list_from_text = my_string.split()
list_from_text_2 = my_string.split(',')
print(list_from_text)
print(list_from_text_2)
print('-' * 20)

language = ['Python', 'Java', 'Ruby']
language = ', '.join(language)
print(language)
print('-' * 20)

a = 'one'
b = 'two'
print('First word is', a, ', second word is', b)

my_text = 'First word is ' + a + ', second word is ' + b
print(my_text)

my_text = 'First word is %s, second word is %s'
print(my_text % (a, b))

my_text = 'First word is {0}, second word is {1}'
print(my_text.format(a, b))

my_text = f'First word is {a}, second word is {b}'
print(my_text)
