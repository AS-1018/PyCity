# дом-1
def build_h1(money, h_price_1, build_num):
    if money >= h_price_1:
        build_num['h1_num'] = build_num['h1_num'] + 1
        money = money - h_price_1
        print("1-этажный дом построен")
    else:
        print(f"Недостаточно денег,  не хватает {h_price_1 - money}")
    return build_num['h1_num'], money


def get_price_h1(h_price_1):
    print(f"Сейчас цена 1-этажного дома составляет {h_price_1}")

# дом-3


def build_h2(money, h_price_2, build_num):
    if money >= h_price_2:
        build_num['h2_num'] = build_num['h2_num'] + 1
        money = money - h_price_2
        print("3-этажный дом построен")
    else:
        print(f"Недостаточно денег,  не хватает {h_price_2 - money}")
    return build_num['h2_num'], money


def get_price_h2(h_price_1):
    print(f"Сейчас цена 1-этажного дома составляет {h_price_1}")

# дом-5


def build_h3(money, h_price_3, build_num):
    if money >= h_price_3:
        build_num['h3_num'] = build_num['h3_num'] + 1
        money = money - h_price_3
        print("5-этажный дом построен")
    else:
        print(f"Недостаточно денег,  не хватает {h_price_3 - money}")
    return build_num['h3_num'], money


def get_price_h3(h_price_3):
    print(f"Сейчас цена 5-этажного дома составляет {h_price_3}")


# магазин
def build_sh(money, sh_price, build_num):
    if money >= sh_price:
        build_num['sh_num'] = build_num['sh_num'] + 1
        money = money - sh_price
        print("магазин построен")
    else:
        print(f"Недостаточно денег,  не хватает {sh_price - money}")
    return build_num['sh_num'], money


def get_price_sh(sh_price):
    print(f"Сейчас цена 5-этажного дома составляет {sh_price}")
