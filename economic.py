from random import *

# формирование цен:


# покупка земли

def s_buy_func(sb):
    sb += randint(-30, 30)
    if sb <= 20:
        sb += 100
    return sb


# продажа земли

def s_sell_func(ss):
    ss += randint(-16, 10)
    if ss <= 20:
        ss += 80
    return ss

# покупка материалов


def b_buy_func(bb):
    bb += randint(-30, 30)
    if bb <= 20:
        bb += 80
    return bb

# продажа материалов


def b_sell_func(bs):
    bs += randint(-16, 10)
    if bs <= 20:
        bs += 50
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
    sh = 0.95 * sb + 0.8 * bb
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
