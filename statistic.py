from build import *

# рассчёт уровня


def get_lvl(h1, lv1, h2, lv2, h3, lv3, sh, lvs,):
    lvl = h1 * lv1 + h2 * lv2 + h3 * lv3 + sh * lvs
    return lvl

# вывод статы


def get_stat(h1, h2, h3, sh, pr, df, ch):
    # рассчёт статы (при каждом запросе считатетсЯ заново)
    houses = h1 + h2 + h3
    # вывод
    print(
        f"\nДоходы:{pr} \nРасходы:{df} \nЗаработок:{ch} \nКол-во всех домов:{houses}")
    print(f"Кол-во 1-этажных домов:{h1} \nКол-во 3-этажных домов:{h2}")
    print(f"Кол-во 5-этажных домов:{h3} \nКол-во магазинов:{sh}\n")

# вывод биржы


def get_birg(s_price_buy, s_price_sell, b_price_buy, b_price_sell):
    print(f"\nЦены на землю \nПокупка:{s_price_buy} \nПродажа:{s_price_sell}")
    print(
        f"Цены на строй. материалы \nПокупка:{b_price_buy} \nПродажа:{b_price_sell}\n")

# вывод команд


def get_cmd():
    print("\nПостроить *название здания* - Построит *здание*")
    print("Цена *название здания* - Цена *здания*")
    print("Список зданий - Выводит список всех зданий и их описание")
    print("Статистика - Вывод статистики \nБиржа - Инфориация о ценах \nСледущий ход(сх) - Перейти на следущий ход")
    print("Сохранить - Сохранит текущее состояние (перезаписывает предыдущее)\n")

# Вывод существующих зданий


def get_buildlist():
    print(f"\n{house1.name} - 1-этажный дом в котором могут жить {house1.pop} человек, сейчас стоит {house1.price}")
    print(f"{house3.name} - 3-этажный дом в котором могут жить {house1.pop} человек, сейчас стоит {house3.price}")
    print(f"{house5.name} - 5-этажный дом в котором могут жить {house1.pop} человек, сейчас стоит {house5.price}")
    print(f"{shop.name} - Небольшой магазин, сейчас стоит {shop.price}\n")

# статус:


def get_status(p, k1, k2, k3, k4, k5, k6, k7):
    if 0 <= p < 50:
        st = "Хутор"
    elif 100 <= p < 200:
        st = "Маленькая деревня"
        k1 += 1
    elif 200 <= p < 1000:
        st = "Средняя деревня"
        k2 += 1
    elif 1000 <= p < 3000:
        st = "Большая деревня"
        k3 += 1
    elif 3000 <= p < 5000:
        st = "Посёлок"
        k4 += 1
    elif 5000 <= p < 50000:
        st = "Маленький город"
        k5 += 1
    elif 50000 <= p < 100000:
        st = "Средний  город"
        k6 += 1
    elif 100000 <= p < 250000:
        st = "Большой город"
        k7 += 1
    return st


def check_status(k1, k2, k3, k4, k5, k6, k7, st, mn):
    if k1 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 20 монет")
        mn += 20
    elif k2 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 40 монет")
        mn += 40
    elif k3 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 80 монет")
        mn += 80
    elif k4 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 160 монет")
        mn += 160
    elif k5 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 320 монет")
        mn += 320
    elif k6 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 640 монет")
        mn += 640
    elif k7 == 1:
        print(
            f"Вашему городу был присвоен статус {st}, вам выдан грант в размере 1280 монет")
        mn += 1280
    return mn
