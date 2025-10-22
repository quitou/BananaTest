# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.

class Flower:

    def __init__(self, name, color, stem_length, price, time_life, type_grow):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.time_life = time_life
        self.type_grow = type_grow


class Camomile(Flower):

    def __init__(self, name, color, stem_length, price, time_life, type_grow, properties, reserv):
        super().__init__(name, color, stem_length, price, time_life, type_grow)
        self.properties = properties
        self.reserv = reserv

class Roses(Flower):

    def __init__(self, name, color, stem_length, price, time_life, type_grow, properties, reserv):
        super().__init__(name, color, stem_length, price, time_life, type_grow)
        self.properties = properties
        self.reserv = reserv

class Tulips(Flower):
    def __init__(self, name, color, stem_length, price, time_life, type_grow, properties, reserv):
        super().__init__(name, color, stem_length, price, time_life, type_grow)
        self.properties = properties
        self.reserv = reserv

class Bouquet:

    def __init__(self, list_flowers, price_bouquet):
        self.list_flowers = list_flowers
        self.price_bouquet = price_bouquet

    def midle_life_time(self):
        day_life = 0
        for x in self.list_flowers:
            day_life += x.time_life
        return round(day_life / len(self.list_flowers), 2)

    def Search_middle_life_time(self):
        mid_lf_time = self.midle_life_time()
        selection = list(filter(lambda x: x.time_life > mid_lf_time, self.list_flowers))
        result = []
        for x in selection:
            result.append(x.name)
        return result

    def sort_time_life(self):
        sort_list = sorted(self.list_flowers, key = lambda x: x.time_life)
        return sort_list

    def sort_color(self):
        sort_list = sorted(self.list_flowers, key = lambda x: x.color)
        return sort_list

    def sort_len_stem(self):
        sort_list = sorted(self.list_flowers, key = lambda x: x.stem_length, reverse=True)
        return sort_list

    def sort_price(self):
        sort_list = sorted(self.list_flowers, key = lambda x: x.price, reverse=True)
        return sort_list

flower_camomile = Camomile('camomile', 'ellow', 30, 100, 3, 'lend', 'tea', False)
flower_rose = Roses('rose', 'red', 20, 250, 6, 'bush', 'beautiful', True)
flower_tulips = Tulips('tulip_fly', 'blue', 25, 80, 8, 'lend','beautiful', False)

bouquet_flowers_1 = Bouquet([flower_camomile, flower_tulips, flower_rose], flower_tulips.price + flower_rose.price + flower_camomile.price)
bouquet_flowers_2 = Bouquet([flower_camomile, flower_tulips], flower_camomile.price + flower_tulips.price)


# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
print(f'Увядание букета примерно произойдёт: {bouquet_flowers_1.midle_life_time()}')

# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).
print(f'Цветы больше среднего времени жизни в букете: {bouquet_flowers_1.Search_middle_life_time()}')
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
#
# (свежесть)
sorted_time_life = bouquet_flowers_1.sort_time_life()
for x in sorted_time_life:
    print(f'Цветок: {x.name}, время увядания: {x.time_life} дней')
# (цвет)
sorted_color = bouquet_flowers_1.sort_color()
for x in sorted_color:
    print(f'Цветок: {x.name}, цвет: {x.color}')
# (длина стебля)
sorted_ln_stem = bouquet_flowers_1.sort_len_stem()
for x in sorted_ln_stem:
    print(f'Цветок: {x.name}, длинна стебля: {x.stem_length}')
# (стоимость)
sorted_ln_stem = bouquet_flowers_1.sort_price()
for x in sorted_ln_stem:
    print(f'Цветок: {x.name}, цена: {x.price}')
