def nb_year(p0, percent, aug, p):
    perc = percent / 100
    year = 0
    pop = p0
    while pop < p:
        pop = pop + (pop * perc) + aug
        year += 1
    print (int(pop))
    return year

nb_year(1500, 5, 100, 5000) # 15
nb_year(1500000, 2.5, 10000, 2000000) # 10
nb_year(1500000, 0.25, 1000, 2000000) # 94