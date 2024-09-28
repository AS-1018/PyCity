# функция подсчёта роста населения
def pop_func(shops, cash, pop, pop_max):
    pop_up = int(shops*0.5+cash/100+pop/10)
    pop += pop_up
    print(pop_up)  # для дэбага раскоментировать
    if pop > pop_max:
        pop = pop_max
    return pop

# функция подсчёта максимального населения


def pm_func(hd1, hn1, hd2, hn2, hd3, hn3):
    pm = hd1 * hn1 + hd2 * hn2 + hd3 * hn3
    return pm
