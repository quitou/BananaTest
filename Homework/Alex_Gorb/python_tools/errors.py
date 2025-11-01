
def calc(x, y):
    try:
        return int(x) / int(y)
    except (ZeroDivisionError, ValueError) as err:
        print(x, y)
        raise err
        # print(err)
        # print('Ошибка ввода данных')
    # except ZeroDivisionError:
    #     print('На ноль делить нельзя')
    # except ValueError:
    #     print('Ошибка ввода данных')


print(calc(input('number'), input('number')))
print('Hello!')
print('-' * 20)