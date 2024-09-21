from random import *

# формирование цен:

# покупка земли


def s_buy_func(sb):
    sb += randint(-15, 10)
    if sb <= 0:
        sb += 20
    return sb


# продажа земли
def s_sell_func(ss):
    ss += randint(-8, 5)
    if ss <= 0:
        ss += 10
    return ss

# покупка материалов


def b_buy_func(bb):
    bb += randint(-15, 10)
    if bb <= 0:
        bb += 15
    return bb

# продажа материалов


def b_sell_func(bs):
    bs += randint(-8, 5)
    if bs <= 0:
        bs += 10
    return bs

# формула цены 1 дом


def h1_func(sb, bb):
    h1 = 0.75 * sb + 0.75 * bb
    return h1

# формула цены 3 дом


def h2_func(sb, bb):
    h2 = sb + 0.75 * bb
    return h2

# формула цены 5 дом


def h3_func(sb, bb):
    h3 = sb + 1.5 * bb
    return h3

# формула цены магазина


def sh_func(sb, bb):
    sh = 0.75*sb + 0.75*bb
    return sh

# рассчёт доходов и расходов:

# доходы


def pr_func(hp1, hp2, hp3, sp, hn1, hn2, hn3, sn):
    pr = hp1 * hn1 + hp2 * hn2 + hp3 * hn3 + sp * sn
    return pr

# расходы


def df_func(hd1, hd2, hd3, sd, hn1, hn2, hn3, sn):
    df = hd1 * hn1 + hd2 * hn2 + hd3 * hn3 + sd * sn
    return df
