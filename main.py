from random import *
from math import *
from economic import *
from population import *
from graphics import *

money = 0
hod = 1
build_num = {     # кол-во зданий
    'h1_num': 3,
    'h2_num': 0,
    'h3_num': 0,
    'sh_num': 0,
}
house1 = {        # характеристика 1-эт дома
    'pop': 4,
    'prof': 5,
    'def': 2,
}
house2 = {        # характеристика 3-эт дома
    'pop': 15,
    'prof': 8,
    'def': 4,
}
house3 = {        # характеристика 5-эт дома
    'pop': 30,
    'prof': 15,
    'def': 6,
}
shop = {          # характеристика магазина
    'pop': 0,
    'prof': 10,
    'def': 12,
}
houses = 0
shops = 0
pop_max = 12
s_price_buy = 22
s_price_sell = 12
b_price_buy = 16
b_price_sell = 10
pop = 6
profit = 0
defit = 0

# инициализация стартовых цен на дома
h_price_1 = h1_func(s_price_buy, b_price_buy)
h_price_2 = h2_func(s_price_buy, b_price_buy)
h_price_3 = h3_func(s_price_buy, b_price_buy)
sh_price = sh_func(s_price_buy, b_price_buy)

logo_draw()
print('\nPyCity Alpha 0.1 by A/S')
name = input('Введите название вашего города:')
print('Введите "команды",что бы увидеть список доступных действий и пояснения к ним')
while True:

    # рассчёт заработка
    profit = pr_func(house1['prof'], house2['prof'], house3['prof'], shop['prof'],
                     build_num['h1_num'], build_num['h2_num'], build_num['h3_num'], shops)
    defit = df_func(house1['def'], house2['def'], house3['def'], shop['def'],
                    build_num['h1_num'], build_num['h2_num'], build_num['h3_num'], shops)
    cash = profit-defit

    # рассчёт населения
    pop_max = pm_func(house1['pop'], house2['pop'], house3['pop'],
                      build_num['h1_num'], build_num['h2_num'], build_num["h3_num"])
    pop = pop_func(shops, cash, pop, pop_max)

    # ввод действия
    mess = input(f"{name}. Ход: {hod}  Денег: {money}  Население: {pop} >")

    match mess.upper():

        # выход
        case 'ВЫЙТИ': break

        # список команд
        case "КОМАНДЫ":
            print("\nПостроить дом-1/3/5 - Построить 1/3/5-этажный дом")
            print("Цена дома-1/3/5 - Цена 1/3/5-этажного дома")
            print(
                "Построить магазин \nЦена магазина \nСтатистика \nБиржа \nСледущий ход(сх)\n")

        # Дом-1
        case "ПОСТРОИТЬ ДОМ-1":
            if money >= h_price_1:
                build_num['h1_num'] = build_num['h1_num'] + 1
                print("1-этажный дом построен")
            else:
                print(f"Недостаточно денег,  не хватает {h_price_1 - money}")

        case "ЦЕНА ДОМА-1": print(f"Сейчас цена 1-этажного дома составляет {h_price_1}")

        # Дом-3
        case "ПОСТРОИТЬ ДОМ-3":
            if money >= h_price_1:
                build_num['h2_num'] = build_num['h2_num'] + 1
                print("3-этажный дом построен")
            else:
                print(f"Недостаточно денег, не хватает {h_price_2 - money}")

        case "ЦЕНА ДОМА-3": print(f"Сейчас цена 3-этажного дома составляет {h_price_2}")

        # Дом-5
        case "ПОСТРОИТЬ ДОМ-5":
            if money >= h_price_1:
                build_num['h3_num'] = build_num['h3_num'] + 1
                print("5-этажный дом построен")
            else:
                print(f"Недостаточно денег,  не хватает {h_price_3 - money}")

        case "ЦЕНА ДОМА-5": print(f"Сейчас цена 5-этажного дома составляет {h_price_3}")

        # Магазин
        case "ПОСТРОИТЬ МАГАЗИН":
            if money >= h_price_1:
                build_num['sh_num'] = build_num['sh_num'] + 1
                print("Магазин построен построен")
            else:
                print(f"Недостаточно денег,  не хватает {sh_price - money}")

        case "ЦЕНА МАГАЗИНА": print(f"Сейчас цена магазина составляет {sh_price}")

        # открытие биржы
        case 'БИРЖА':
            print(
                f"\nЦены на землю \nПокупка:{s_price_buy} \nПродажа:{s_price_sell}")
            print(
                f"Цены на строй. материалы \nПокупка:{b_price_buy} \nПродажа:{b_price_sell}\n")

        case 'СТАТИСТИКА':
            # рассчёт статы (при каждом запросе считатетсЯ заново)
            houses = build_num['h1_num'] + \
                build_num['h2_num'] + build_num['h3_num']
        # вывод статы
            print(
                f"\nДоходы:{profit} \nРасходы:{defit} \nЗаработок:{cash} \nКол-во всех домов:{houses}")
            print(
                f"Кол-во 1-этажных домов:{build_num['h1_num']} \nКол-во 3-этажных домов:{build_num['h2_num']}")
            print(
                f"Кол-во 5-этажных домов:{build_num['h3_num']} \nКол-во магазинов:{build_num['sh_num']}\n")

        case 'СЛЕДУЩИЙ ХОД' | 'СХ':
           # console_clear \не работает
            houses = 0
            hod += 1
            money += cash
        # формирование цен на следущий ход //БИРЖА
            s_price_buy = s_buy_func(s_price_buy)
            s_price_sell = s_sell_func(s_price_sell)
            b_price_buy = b_buy_func(b_price_buy)
            b_price_sell = b_sell_func(b_price_sell)
        # формирование цен на следущий ход //ПОСТРОЙКИ
            h_price_1 = h1_func(s_price_buy, b_price_buy)
            h_price_2 = h2_func(s_price_buy, b_price_buy)
            h_price_3 = h3_func(s_price_buy, b_price_buy)
            sh_price = sh_func(s_price_buy, b_price_buy)

        case other:
            print('Такой команды не существует,проверьте,правильно ли ввели команду')
