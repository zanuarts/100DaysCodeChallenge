def tower_builder(n_floors):
    tower = []
    if n_floors == 0:
        return []
    for i in range(1, n_floors + 1):
        star = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        tower.append(space + star + space)
        
    return tower

tower_builder(1) # ['*', ]
tower_builder(2) # [' * ', '***']
tower_builder(3) # ['  *  ', ' *** ', '*****']