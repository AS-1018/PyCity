from economic import *
from population import *
from graphics import *
from statistic import *
from build import *
from random import randint

# меню

logo_draw()

print("\nWelcome to PyCity Alpha 0.2r1 by A/S")
print("\n1. Начать новую игру")
print("2. Продолжить последнюю игру")
print("3. Выйти ")
msg = int(input("\nВыберите пункт меню: "))

if msg == 1:

    name = input('\nВведите название населённого пункта:')
    get_plot(name)
    print('Введите "команды",что бы увидеть список доступных действий и пояснения к ним')

    money = 0
    hod = 1
    pop_max = 12
    s_price_buy = randint(90, 140)
    s_price_sell = s_price_buy - randint(10, 25)
    b_price_buy = randint(70, 100)
    b_price_sell = s_price_buy - randint(10, 25)
    pop = 6
    profit = 0
    efit = 0
    cash = 0

    # инициализация цен на дома
    house1.calc_price(s_price_buy, b_price_buy)
    house3.calc_price(s_price_buy, b_price_buy)
    house5.calc_price(s_price_buy, b_price_buy)
    shop.calc_price(s_price_buy, b_price_buy)
    # рассчёт заработка
    profit = pr_func(house1.profit, house3.profit, house5.profit, shop.profit,
                     house1.num, house3.num, house5.num, shop.num)
    defit = df_func(house1.defit, house3.defit, house5.profit, shop.profit,
                    house1.num, house3.num, house5.num, shop.num)
    cash = profit - defit

elif msg == 2:

    print('\nВведите "команды",что бы увидеть список доступных действий и пояснения к ним')

    f = open('save.txt', 'r')
    try:

        name = str(f.readlines(1))  # название города
        name = name.replace('name = ', '')
        name = name[2:-4]

        money = str(f.readlines(2))  # деньги
        money = money.replace('money = ', '')
        money = int(money[2:-4])

        hod = str(f.readlines(3))  # ход
        hod = hod.replace('hod = ', '')
        hod = int(hod[2:-4])

        pop = str(f.readlines(4))  # население
        pop = pop.replace('pop = ', '')
        pop = int(pop[2:-4])

        h1 = str(f.readlines(5))  # колво домов-1
        h1 = h1.replace('house1 = ', '')
        h1 = int(h1[2:-4])
        house1.num = h1

        h3 = str(f.readlines(6))  # колво домов-3
        h3 = h3.replace('house3 = ', '')
        h3 = int(h3[2:-4])
        house3.num = h3

        h5 = str(f.readlines(7))  # колво домов-5
        h5 = h5.replace('house5 = ', '')
        h5 = int(h5[2:-4])
        house5.num = h5

        sh = str(f.readlines(8))  # колво магазинов
        sh = sh.replace('shop = ', '')
        sh = int(sh[2:-4])
        shop.num = sh

        s_price_buy = str(f.readlines(9))  # покупка земли
        s_price_buy = s_price_buy.replace('space_buy = ', '')
        s_price_buy = int(s_price_buy[2:-4])

        s_price_sell = str(f.readlines(10))  # покупка продажа
        s_price_sell = s_price_sell.replace('space_sell = ', '')
        s_price_sell = int(s_price_sell[2:-4])

        b_price_buy = str(f.readlines(11))  # покупка инструментов
        b_price_buy = b_price_buy.replace('buildinst_buy = ', '')
        b_price_buy = int(b_price_buy[2:-4])

        b_price_sell = str(f.readlines(12))  # продажа инструментов
        b_price_sel = b_price_sell.replace('buildinst_sell = ', '')
        b_price_sell = int(b_price_sel[2:-4])

    finally:
        f.close()

    pop_max = pm_func(house1.pop, house3.pop, house5.pop,
                      house1.num, house3.num, house5.num)

    # инициализация цен на дома
    house1.calc_price(s_price_buy, b_price_buy)
    house3.calc_price(s_price_buy, b_price_buy)
    house5.calc_price(s_price_buy, b_price_buy)
    shop.calc_price(s_price_buy, b_price_buy)
    # рассчёт заработка
    profit = pr_func(house1.profit, house3.profit, house5.profit, shop.profit,
                     house1.num, house3.num, house5.num, shop.num)
    defit = df_func(house1.defit, house3.defit, house5.profit, shop.profit,
                    house1.num, house3.num, house5.num, shop.num)
    cash = profit - defit


elif msg == 3:
    exit


# игра

while True:

    # рассчёт заработка
    profit = pr_func(house1.profit, house3.profit, house5.profit, shop.profit,
                     house1.num, house3.num, house5.num, shop.num)
    defit = df_func(house1.defit, house3.defit, house5.profit, shop.profit,
                    house1.num, house3.num, house5.num, shop.num)
    cash = profit - defit

    # ввод действия
    cmd = input(f"{name}. Ход: {hod}  Деньги: {money}  Население: {pop} >")

    match cmd.upper():

        # выход
        case 'ВЫЙТИ': break

    # список команд
        case "КОМАНДЫ": get_cmd()

    # Дом-1
        case "ПОСТРОИТЬ ДОМ-1": house1.num, money = house1.buy_new(money)

        case "ЦЕНА ДОМА-1": house1.get_price()

        case "СНЕСТИ ДОМ-1": house1.remove()

    # Дом-3
        case "ПОСТРОИТЬ ДОМ-3": house3.num, money = house3.buy(money)

        case "ЦЕНА ДОМА-3": house3.get_price()\

        case "СНЕСТИ ДОМ-3": house3.remove()

    # Дом-5
        case "ПОСТРОИТЬ ДОМ-5": house5.num, money = house5.buy(money)

        case "ЦЕНА ДОМА-5": house5.get_price()

        case "СНЕСТИ ДОМ-5": house5.remove()

    # Магазин
        case "ПОСТРОИТЬ МАГАЗИН": shop.num, money = shop.buy(money)

        case "ЦЕНА МАГАЗИНА": shop.get_price()

        case "СНЕСТИ МАГАЗИН": shop.remove()

    # открытие биржы
        case 'БИРЖА': get_birg(s_price_buy, s_price_sell, b_price_buy, b_price_sell)

    # Открытее статы
        case 'СТАТИСТИКА': get_stat(house1.num, house3.num, house5.num,
                                    shop.num, profit, defit, cash)

    # Вывод спика зданий
        case "СПИСОК ЗДАНИЙ": get_buildlist()

    # следущий ход
        case 'СЛЕДУЩИЙ ХОД' | 'СХ':

            hod += 1

    # рассчёт населения
            pop_max = pm_func(house1.pop, house3.pop, house5.pop,
                              house1.num, house3.num, house5.num)
            pop = pop_func(shop.num, cash, pop, pop_max)

            money += cash

            # формирование цен на следущий ход //БИРЖА
            s_price_buy = s_buy_func(s_price_buy)
            s_price_sell = s_sell_func(s_price_sell)
            b_price_buy = b_buy_func(b_price_buy)
            b_price_sell = b_sell_func(b_price_sell)
            # формирование цен на следущий ход //ПОСТРОЙКИ
            house1.calc_price(s_price_buy, b_price_buy)
            house3.calc_price(s_price_buy, b_price_buy)
            house5.calc_price(s_price_buy, b_price_buy)
            shop.calc_price(s_price_buy, b_price_buy)

        # сохранение игры
        case "СОХРАНИТЬ":
            f = open('save.txt', 'w')

            f.write(f"name = {name}\n")
            f.write(f"money = {money}\n")
            f.write(f"hod = {hod}\n")
            f.write(f"pop = {pop}\n")
            f.write(f"house1 = {house1.num}\n")
            f.write(f"house3 = {house3.num}\n")
            f.write(f"house5 = {house5.num}\n")
            f.write(f"shop = {shop.num}\n")
            f.write(f"space_buy = {s_price_buy}\n")
            f.write(f"space_sell = {s_price_sell}\n")
            f.write(f"buildinst_buy = {b_price_buy}\n")
            f.write(f"buildinst_sell = {b_price_sell}\n")

            f.close()

        case other:
            print(
                f'Команды {cmd} не существует, проверьте,правильно ли ввели команду')
