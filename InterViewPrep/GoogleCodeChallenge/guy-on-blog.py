def answer(population, x, y, strength):
    if population[y][x] <= strength:
    # If patient zero is susceptible to the disease, represent with -1
    population[y][x] = -1
    # Call spread function to initiate spread of infection
    spread(population, x, y, strength)
    return population

def spread(population, x, y, strength):
    ''' Spread will will recursively search through matrix and 
    continue or cease depending upon rabbit resistance level
    and infection strength ''' 
    # Look at the rabbit to left
    if x != 0 and population[y][x - 1] <= strength and population[y][x - 1] != -1:              
        population[y][x - 1] = -1       
        spread(population, x - 1, y, strength)  

    # Look at the rabbit to the right
    if len(population[0]) > x + 1 and population[y][x + 1] <= strength and population[y][x + 1]   
    != -1:
    population[y][x + 1] = -1
    spread(population, x + 1, y, strength)

    # Look at rabbit above
    if y != 0 and population[y - 1][x] <= strength and population[y - 1][x] != -1:      
        population[y - 1][x] = -1
        spread(population, x, y - 1, strength)

    # Look at the rabbit below
    if len(population) > y + 1 and population[y + 1][x] <= strength and population[y + 1][x] !=  
    -1:
    population[y + 1][x] = -1
    spread(population, x, y + 1, strength)
#p1 = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
p1 = [[6, 7,4], [6, 3, 1, 4, 7], [0, 2, 4, 1, 3, 2], [8, 1, 1, 4, 9], [1,2,3,2,2,2,2,2,6,2,2,2,],[3]]
for a in p1:
    print a
print 
p2 = answer(p1,0,0,7)
for a in p2:
    print a