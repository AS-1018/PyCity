from economic import *
from population import *
from graphics import *
from statistic import *
from build import *
from manage import *

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
    'lvl': 10,
}
house2 = {        # характеристика 3-эт дома
    'pop': 15,
    'prof': 8,
    'def': 4,
    'lvl': 15,
}
house3 = {        # характеристика 5-эт дома
    'pop': 30,
    'prof': 15,
    'def': 6,
    'lvl': 30,
}
shop = {          # характеристика магазина
    'pop': 0,
    'prof': 10,
    'def': 2,
    'lvl': 20,
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
cash = 0
st = ''

# инициализация стартовых цен на дома
h_price_1 = h1_func(s_price_buy, b_price_buy)
h_price_2 = h2_func(s_price_buy, b_price_buy)
h_price_3 = h3_func(s_price_buy, b_price_buy)
sh_price = sh_func(s_price_buy, b_price_buy)
# определение начального опыта
lvl = get_lvl(build_num['h1_num'], house1['lvl'], build_num['h2_num'], house2['lvl'],
              build_num['h3_num'], house3['lvl'], build_num['sh_num'], shop['lvl'],)
# Определение начального статуса
status = get_status(lvl)
# рассчёт начального заработка
profit = pr_func(house1['prof'], house2['prof'], house3['prof'], shop['prof'],
                 build_num['h1_num'], build_num['h2_num'], build_num['h3_num'], shops)
defit = df_func(house1['def'], house2['def'], house3['def'], shop['def'],
                build_num['h1_num'], build_num['h2_num'], build_num['h3_num'], shops)
cash = profit - defit

logo_draw()

print('\nPyCity Alpha 0.1.0.1 by A/S')
name = input('Введите название вашего города:')
print('Введите "команды",что бы увидеть список доступных действий и пояснения к ним')
while True:

    # рассчёт заработка
    profit = pr_func(house1['prof'], house2['prof'], house3['prof'], shop['prof'],
                     build_num['h1_num'], build_num['h2_num'], build_num['h3_num'], shops)
    defit = df_func(house1['def'], house2['def'], house3['def'], shop['def'],
                    build_num['h1_num'], build_num['h2_num'], build_num['h3_num'], shops)
    cash = profit - defit

    # ввод действия
    mess = input(f"{name}. Ход: {hod}  Денег: {money}  Население: {pop} >")

    match mess.upper():

        # выход
        case 'ВЫЙТИ': break

        # список команд
        case "КОМАНДЫ": get_cmd()

        # Дом-1
        case "ПОСТРОИТЬ ДОМ-1":
            build_num['h1_num'], money = build_h1(money, h_price_1, build_num)

        case "ЦЕНА ДОМА-1": get_price_h1(h_price_1)

        # Дом-3
        case "ПОСТРОИТЬ ДОМ-3":
            build_num['h2_num'], money = build_h2(money, h_price_2, build_num)

        case "ЦЕНА ДОМА-3": get_price_h2(h_price_2)

        # Дом-5
        case "ПОСТРОИТЬ ДОМ-5":
            build_num['h3_num'], money = build_h3(money, h_price_3, build_num)

        case "ЦЕНА ДОМА-5": get_price_h3(h_price_3)

        # Магазин
        case "ПОСТРОИТЬ МАГАЗИН":
            build_num['sh_num'], money = build_sh(money, sh_price, build_num)

        case "ЦЕНА МАГАЗИНА":  get_price_sh(sh_price)

        # открытие биржы
        case 'БИРЖА': get_birg(s_price_buy, s_price_sell, b_price_buy, b_price_sell)

        case 'СТАТИСТИКА': get_stat(build_num['h1_num'], build_num['h2_num'], build_num['h3_num'],
                                    build_num['sh_num'], profit, defit, cash, lvl, status)

        case 'СЛЕДУЩИЙ ХОД' | 'СХ': houses, hod, money, cash, s_price_buy, s_price_sell, b_price_buy, b_price_sell, h_price_1, h_price_2, h_price_3, sh_price, build_num, shops, pop, pop_max = nt(houses,
                                                                                                                                                                                                   hod, money, cash, s_price_buy, s_price_sell, b_price_buy, b_price_sell, h_price_1, h_price_2, h_price_3, sh_price, build_num, house1, house2, house3, shop, shops, pop, pop_max)
        case other:
            print('Такой команды не существует,проверьте,правильно ли ввели команду')
