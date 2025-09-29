# user_input = int(input('your number: '))
#
# if user_input.isnumeric():
#     user_input = int(user_input)
#     if user_input == 1:
#         print('One')
#     elif user_input == 2:
#         print('Two')
#     else:
#         print('Many')
# else:
#     print('Enter number please')

# if user_input > 0:
#     if user_input > 1:
#         if user_input == 2:
#             print()
#         elif user_input == 3:
#             if 1 == 1:
#                 print()
#             elif 2 == 2:
#                 print()
#     elif 3 == 3:
#         print()

names =['John', 'Tom', 'James', 'Bob', 'Tim', 'Bill']

for name in names:
    print(name)

print('-' * 20)

for name in names:
    if name.startswith('J'):
        print('Mr.', end =' ')
    print(name)

print('-' * 20)

persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons.values():
    print(person)

print('-' * 20)

persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons:
    print(f'{person}: {persons[person]}')

print('-' * 20)

for person in persons.items():
    name, height = person
    print(f'{name}: {height}')

print('-' * 20)

for name, height in persons.items():
    print(f'{name}: {height}')

print('-' * 20)

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'
words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word)
print(' '.join(fin_words))
