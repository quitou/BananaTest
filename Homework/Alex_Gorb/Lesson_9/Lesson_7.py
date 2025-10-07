import sys
from random import random, randint, randrange, choice

from Homework.Alex_Gorb.Lesson_9.utils.assistent import assist

# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(0, 2))
# users = ['user1', 'user2', 'user100']
# print(random.choice(users))

print(random())
print(randint(0, 5))
print(randrange(0, 2))
users = ['user1', 'user2', 'user100']
print(choice(users))

print(sys.platform)
assist()
# print(assistent.variable)