class building():  # класс зданий

    def __init__(self, num, name, pop, profit, defit, price, const_space, const_build):

        self.num = num  # кол-во
        self.name = name  # название здания
        self.pop = pop  # максимум жителей
        self.profit = profit  # сколько денег приносит // заменить на систему налогов
        self.defit = defit  # сколько денег потребляет // заменить на систему потребностей
        self.price = price  # цена
        self.const_space = const_space  # коэфицент при покупки относительно цены земли
        # коэфицент при покупки относительно цены оборудования
        self.const_build = const_build

    # рассчёт цены
    def calc_price(self, space, build) -> float:
        self.price = self.const_space * space + self.const_build * build
        self.price = round(self.price, 2)
        return self.price

    # вывод цены
    def get_price(self):
        print(f"Сейчас цена {self.name} составляет {self.price}")

    # покупка
    def buy(self, money):
        if money >= self.price:
            money -= self.price
            self.num += 1
            print(f"Здание {self.name} было построен")
        else:
            print(
                f"Для постройки здания {self.name} не хватает {self.price - money}")
        return self.num, money

    def buy_new(self, money: float) -> float:
        if money >= self.price:
            self.num = self.num + 1
            money = money - self.price
            print(f"{self.name} построен")
        else:
            print(f"Недостаточно денег,  не хватает {self.price - money}")
        return self.num, money

    # снос

    def remove(self):
        self.num -= 1
        print(f"{self.name} снесён")
        return self.num


# 1-этажный дом
house1 = building(3, "1-этажный дом", 5, 10, 4, 0, 0.75, 0.75)

# 3-этажный-дом
house3 = building(0, "3-этажный дом", 15, 16, 8, 0, 1, 0.75)

# 5-этажный дом
house5 = building(0, "5-этажный дом", 30, 30, 12, 0, 1, 1.5)

# магазин
shop = building(0, "Магазин", 0, 20, 6, 0, 0.95, 0.8)
