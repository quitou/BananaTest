def generate_text(text1, text2):
    return f'Text consists on wthe words:{text1} and {text2}'

print(generate_text('Ivan', 'Ivanov'))

my_list = [1, 2, 6 ,7 ,15, 22]

for x in my_list:
    print(x)

print('_' * 20)

#n = 2

#progression = []
#num = 1
# while len(progression) < 10000000:
#     progression.append(num)
#     num += n

def progression(limit = 100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

# for number in progression(10):
#     print(number)

count_progress = 1
for number in progression(1000001):
    if count_progress == 1000000:
        print(number)
        break
    count_progress += 1