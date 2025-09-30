import random

# Задание №1 - "Угадайка"
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
#
# Подсказка: задание выполняется с помощью цикла while

# TODO: Original homework.
min_num = 0
max_num = 10
hidden_number = random.randint(min_num, max_num)

print(f"Guess the hidden number! It's in range: {min_num} - {max_num}.\n")
while True:
    try:
        user_numb = int(input('Enter your number: '))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if user_numb == hidden_number:
        print('You guessed the number')
        break
    else:
        print('Wrong number')
