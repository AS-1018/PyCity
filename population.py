# функция подсчёта роста населения

def pop_func(shops, cash, pop, pop_max):
    pop_up = int(shops*0.5+cash/40+pop/10)
    pop += pop_up
    print(pop_up)  # для дэбага раскоментировать
    if pop > pop_max:
        pop = pop_max
    return pop

# функция подсчёта максимального населения


def pm_func(hp1, hp2, hp3, hn1, hn2, hn3):
    pm = hp1 * hn1 + hp2 * hn2 + hp3 * hn3
    print(pm)
    return pm
