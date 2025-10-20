from abc import abstractmethod

class Group:
    pupils = True
    school_name = 42
    director = 'Marivanna'

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader

    def study(self):
        print('sit down and read')

    @abstractmethod
    def move(self):
        pass

class PrimaryGroup(Group):
    max_age = 11
    min_ame = 6
    building_section = 'left'

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room

    def move(self):
        print('Run fast')

class HighGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('Go slowly')

class MediumGroup(Group):
    max_age = 15
    min_age = 10

first_a = PrimaryGroup('1a', 18, 'MF', 5)
first_b = PrimaryGroup('1b', 20, 'TD', 8)
eleven_a = HighGroup('11a', 10, 'FF')
six_a = MediumGroup('6a', 25, 'RF')


print(first_a.title, first_a.pupils_count, first_a.group_leader)
print(first_a.pupils)
print(first_a.school_name)
print(first_a.min_ame)
print(first_a.max_age)
print(first_a.director)
print(first_a.building_section)
first_a.study()
first_a.move()
eleven_a.move()
six_a.move()
print(first_a.class_room)