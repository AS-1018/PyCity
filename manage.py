from economic import *
from statistic import *
from population import *


def nt(houses, hod, money, cash, s_price_buy, s_price_sell, b_price_buy, b_price_sell, h_price_1, h_price_2, h_price_3, sh_price, build_num, house1, house2, house3, shop, pop, pop_max, lvl, st):
    houses = 0
    hod += 1
    # рассчёт населения
    pop_max = pm_func(house1['pop'], house2['pop'], house3['pop'],
                      build_num['h1_num'], build_num['h2_num'], build_num["h3_num"])
    pop = pop_func(build_num['sh_num'], cash, pop, pop_max)
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
    # определение опыта
    lvl = get_lvl(build_num['h1_num'], house1['lvl'], build_num['h2_num'], house2['lvl'],
                  build_num['h3_num'], house3['lvl'], build_num['sh_num'], shop['lvl'],)
    # Определение статуса
    st = get_status(lvl)
    return houses, hod, money, cash, s_price_buy, s_price_sell, b_price_buy, b_price_sell, h_price_1, h_price_2, h_price_3, sh_price, build_num,  pop, pop_max, lvl, st
