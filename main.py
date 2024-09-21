from random import *
from math import *
from economic import *
from array import * 

money = 0
hod = 1
house_num = array ('i',[3,0,0])
house1 = array ('i',[4,5,2])
house2 = array ('i',[15,8,4])
house3 = array ('i',[30,15,6])
shop = array ('i',[10,1])
houses = 0
shops = 100
pop = 6
pop_max = 12
profit = 15
defit = 6
s_price_buy = 22
s_price_sell = 12
b_price_buy = 16
b_price_sell = 10

#инициализация стартовых цен на дома
h_price_1 = h1_func(s_price_buy,b_price_buy)
h_price_2 = h2_func(s_price_buy,b_price_buy)
h_price_3 = h3_func(s_price_buy,b_price_buy)
sh_price = sh_func(s_price_buy,b_price_buy)

#функция подсчёта роста населения
def pop_func(shops,cash,pop,pop_max):
	pop_up=shops*0.5+cash/100+pop/10
	pop += pop_up
	print(pop_up)
	if pop > pop_max:pop = pop_max
	return pop
	
print('PyCity Alpha 0.1r21 by A/S')
name = input('Введите название вашего города:')
print('Введите "команды",что бы увидеть список доступных действий и пояснения к ним')
while True:
	
	#рассчёт заработка
	cash=profit-defit

	#ввод действия
	mess=input(f"{name}. Ход: {hod}  Денег: {money}  Население: {pop} >")

	match mess.upper():

		#список команд
		case "КОМАНДЫ":
			print("Построить дом/1/3/5 - Построить 1/3/5-этажный дом \nЦена дома/1/3/5 - Цена 1/3/5-этажного дома\nПостроить магазин \nЦена магазина \nСтатистика \nБиржа \nСледущий ход(сх)")
		
		#выход
		case 'ВЫЙТИ':break

		#открытие биржы	
		case 'БИРЖА':
			print(f"Цены на землю \nПокупка:{s_price_buy} \nПродажа:{s_price_sell}")
			print(f"Цены на строй. материалы \nПокупка:{b_price_buy} \nПродажа:{b_price_sell}")

		
		case 'СТАТИСТИКА':
		#рассчёт статы (при каждом запросе считатетсЯ заново)
			for i in range(len(house_num)):
				houses+=house_num[i]
		#вывод статы
			print(f"Доходы:{profit} \nРасходы:{defit} \nЗаработок{cash} \nКол-во всех домов:{houses} \nКол-во 1-этажных домов:{house_num[0]} \nКол-во 3-этажных домов:{house_num[1]} \nКол-во 5-этажных домов:{house_num[2]} \nКол-во магазинов:{shops}")

		
		case 'СЛЕДУЩИЙ ХОД'|'СХ':
				houses = 0
				hod+=1
				money+=cash		
		#формирование цен на следущий ход //БИРЖА
				s_price_buy = s_buy_func(s_price_buy)
				s_price_sell = s_sell_func(s_price_sell)
				b_price_buy = b_buy_func(b_price_buy)
				b_price_sell = b_sell_func(b_price_sell)
		#формирование цен на следущий ход //ПОСТРОЙКИ
				h_price_1 = h1_func(s_price_buy,b_price_buy)
				h_price_2 = h2_func(s_price_buy,b_price_buy)
				h_price_3 = h3_func(s_price_buy,b_price_buy)
				sh_price = sh_func(s_price_buy,b_price_buy)
		#рассчёт населения
				pop = pop_func(shops,cash,pop,pop_max)

		case other :
			print('Такой команды не существует,проверьте,правильно ли ввели команду')
	
		
		
	