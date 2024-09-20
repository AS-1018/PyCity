from random import *
from math import *
from Economic import * 

money = 0
hod = 1
houses = 3
houses_1= 3
houses_2 = 0
houses_3 = 0
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
	
print('PyCity test2 by A/S')
name = input('Введите название вашего города:')
print('Введите "команды",что бы увидеть список доступных действий и пояснения к ним')
while True:
	

	
	#ввод действия
	mess=input(f"{name}. Ход: {hod}  Денег: {money}  Население: {pop}")
	
	#список команд
	if mess.upper() == "КОМАНДЫ":
		print("Построить дом/1/3/5 - Построить 1/3/5-этажный дом \nЦена дома/1/3/5 - Цена 1/3/5-этажного дома\nПостроить магазин \nЦена магазина \nСтатистика \nБиржа \nСледущий ход(сх)")
	
	#выход
	elif mess.upper() == 'ВЫЙТИ':break
	
	#построить 1 дом
	elif mess.upper() == 'ПОСТРОИТЬ  ДОМ/1' and money >= h_price_1:
		houses_1+=1
		pop_max+=4
		profit+=5
		defit+=2
	elif mess.upper() == 'ПОСТРОИТЬ ДОМ/1' and money < h_price_1:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА ДОМА/1':
		print(f"Цена 1-этажного дома сегодня:{h_price_1}")
		
	#построить 3 дом
	elif mess.upper() == 'ПОСТРОИТЬ  ДОМ/3' and money >= h_price_2:
		houses_2+=1
		pop_max+=15
		profit+=8
		defit+=4
	elif mess.upper() == 'ПОСТРОИТЬ ДОМ/3' and money < h_price_2:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА ДОМА/3':
		print(f"Цена 1-этажного дома сегодня:{h_price_2}")
		
	#построить 5 дом
	elif mess.upper() == 'ПОСТРОИТЬ  ДОМ/5' and money >= h_price_3:
		houses_3+=1
		pop_max+=30
		profit+=15
		defit+=6
	elif mess.upper() == 'ПОСТРОИТЬ ДОМ/5' and money < h_price_3:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА ДОМА/5':
		print(f"Цена 1-этажного дома сегодня:{h_price_3}")
		
		#постройка магазина
	elif mess.upper() == 'ПОСТРОИТЬ МАГАЗИН' and money >= sh_price:
		shops+=1
		profit+=10
		defit+=1
	elif mess.upper() == 'ПОСТРОИТЬ МАГАЗИН' and money < sh_price:
			print('Недостаточно средств')
		
	elif mess.upper() == 'ЦЕНА МАГАЗИНА':
		print(f"Цена магазина сегодня:{sh_price}")
	

	#вызов статы
	elif mess.upper() == 'СТАТИСТИКА':
		print(f"Доходы:{profit} \nРасходы:{defit} \nКол-во домов:{houses} \nКол-во магазинов{shops}")
		
	#открытие биржы
	elif mess.upper() == 'БИРЖА':
		print(f"Цены на землю \nПокупка:{s_price_buy} \nПродажа:{s_price_sell}")
		print(f"Цены на строй. материалы \nПокупка:{b_price_buy} \nПродажа{b_price_sell}")
		
	#счётчик ходов 
	elif mess.upper() == 'СЛЕДУЩИЙ ХОД' or mess.upper() == 'СХ':
		hod+=1
		cash=profit-defit
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
		
	 #вывод всех переменных на случай ошибок P.S Выводит не всё
	elif mess.upper() == 'DEBUG':
		print(f"money:{money} \nhod:{hod} \nhouses_1:{houses_1} \nhouses_2:{houses_2} \nhouses_3:{houses_3} \npop:{pop} \npop_max:{pop_max} \npop_up:{pop_up}'")
	else:print('Такой команды не существует,убедитесь,что вы ввели всё правильно')
	