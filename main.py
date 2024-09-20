from random import *
from math import *
from economic import *
from array import * 

money = 0
hod = 1
house_num = array ('i',[3,0,0])
houses = 0
shops = 0
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
def pop_func(shops,cash,pop):
	pop_up=floor(shops*0.5+cash/100+pop/10)
	return pop_up
	
print('PyCity Alpha 0.1e by A/S')
name = input('Введите название вашего города:')
print('Введите "команды",что бы увидеть список доступных действий и пояснения к ним')
while True:
	
	#рассчёт заработка
	cash=profit-defit

	#ввод действия
	mess=input(f"{name}. Ход: {hod}  Денег: {money}  Население: {pop} >")
	
	#список команд
	if mess.upper() == "КОМАНДЫ":
		print("Построить дом/1/3/5 - Построить 1/3/5-этажный дом \nЦена дома/1/3/5 - Цена 1/3/5-этажного дома\nПостроить магазин \nЦена магазина \nСтатистика \nБиржа \nСледущий ход(сх)")
	
	#выход
	elif mess.upper() == 'ВЫЙТИ':break
	
	#построить 1 дом
	elif mess.upper() == 'ПОСТРОИТЬ  ДОМ/1' and money >= h_price_1:
		house_num[0]+=1
		pop_max+=4
		profit+=5
		defit+=2
		print('1-этажный дом построен')

	elif mess.upper() == 'ПОСТРОИТЬ ДОМ/1' and money < h_price_1:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА ДОМА/1':
		print(f"Цена 1-этажного дома сегодня:{h_price_1}")
		
	#построить 3 дом
	elif mess.upper() == 'ПОСТРОИТЬ  ДОМ/3' and money >= h_price_2:
		house_num[1]+=1
		pop_max+=15
		profit+=8
		defit+=4
		print('3-этажный дом построен')

	elif mess.upper() == 'ПОСТРОИТЬ ДОМ/3' and money < h_price_2:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА ДОМА/3':
		print(f"Цена 3-этажного дома сегодня:{h_price_2}")
		
	#построить 5 дом
	elif mess.upper() == 'ПОСТРОИТЬ  ДОМ/5' and money >= h_price_3:
		house_num[2]+=1
		pop_max+=30
		profit+=15
		defit+=6
		print('5-этажный дом построен')

	elif mess.upper() == 'ПОСТРОИТЬ ДОМ/5' and money < h_price_3:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА ДОМА/5':
		print(f"Цена 1-этажного дома сегодня:{h_price_3}")
		
		#постройка магазина
	elif mess.upper() == 'ПОСТРОИТЬ МАГАЗИН' and money >= sh_price:
		shops+=1
		profit+=10
		defit+=1
		print('магазин построен')

	elif mess.upper() == 'ПОСТРОИТЬ МАГАЗИН' and money < sh_price:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА МАГАЗИНА':
		print(f"Цена магазина сегодня:{sh_price}")
	
	#открытие биржы
	elif mess.upper() == 'БИРЖА':
		print(f"Цены на землю \nПокупка:{s_price_buy} \nПродажа:{s_price_sell}")
		print(f"Цены на строй. материалы \nПокупка:{b_price_buy} \nПродажа:{b_price_sell}")

		#вызов статы
	elif mess.upper() == 'СТАТИСТИКА':
		#рассчёт статы
		for i in range(len(house_num)):
			houses+=house_num[i]
		
		print(f"Доходы:{profit} \nРасходы:{defit} \nЗаработок{cash} \nКол-во всех домов:{houses} \nКол-во 1-этажных домов:{house_num[0]} \nКол-во 3-этажных домов:{house_num[1]} \nКол-во 5-этажных домов:{house_num[2]} \nКол-во магазинов{shops}")
		
	#счётчик ходов 
	elif mess.upper() == 'СЛЕДУЩИЙ ХОД' or mess.upper() == 'СХ':
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
	else:
		print('Такой команды не существует,проверьте,правильно ли ввели команду')
	
		
		
	