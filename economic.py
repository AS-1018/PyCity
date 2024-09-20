#формирование цен

from random import *

#покупка земли
def s_buy_func (sb):
    sb += randint(-15,10) 
    if sb<= 0: 
        sb+=20
    return sb
 

#продажа земли
def s_sell_func (ss):
    ss += randint(-8,5)
    if ss<= 0: 
        ss+=10
    return ss

#покупка материалов
def b_buy_func (bb):
    bb += randint(-15,10)
    if bb <= 0: 
        bb+=15
    return bb

#продажа материалов
def b_sell_func (bs):
    bs += randint(-8,5)
    if bs <= 0: 
        bs+=10
    return bs

#формула цены 1 дом
def h1_func(sb,bb):
    h1= 0.75 *sb + 0.75* bb
    return h1

#формула цены 3 дом
def h2_func(sb,bb):
    h2= sb + 0.75* bb
    return h2

#формула цены 5 дом
def h3_func(sb,bb):
    h3= sb + 1.5* bb
    return h3

#формула цены магазина
def sh_func(sb,bb):
    sh = 0.75*sb + 0.75*bb
    return sh