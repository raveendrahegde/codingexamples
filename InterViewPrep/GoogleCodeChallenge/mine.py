def answer(population, x, y, strength):
    try: #Verify gave me an indexerror in next if statement!!!
        population[x][y]
    except:
        return population
        
    if population[x][y] > strength:
        return population
    else:
        population[x][y] = -1
        neighbors = find_week_neighbors(population, x, y, strength)
        infect_neighbors(population, neighbors, strength)
    return population
        
def infect_neighbors(population, neighbors, strength):
    if neighbors:
        for neighbor in neighbors:
            population[neighbor[0]][neighbor[1]] = -1
            #Recursively check week neighbors and infect them
            infect_neighbors(population, find_week_neighbors(population, neighbor[0], neighbor[1], strength), strength)
    else:
        return population
    
def find_week_neighbors(population, x, y, strength):
    neighbors = []
    rowlen = len(population[x])
    collen = len(population)
    if y > 0: #Only if has something on the left
        if population[x][y-1] <= strength and population[x][y-1] != -1: #Ignore if already infected
            l = (x, y-1)
            neighbors.append(l)
    if y < rowlen -1:
        if population[x][y+1] <= strength and population[x][y+1] != -1:
            r = (x, y+1)
            neighbors.append(r)
    if x > 0 and len(population[x-1]) > y:
        if population[x-1][y] <= strength and population[x-1][y] != -1:
            u = (x-1, y)
            neighbors.append(u)
    if x < collen -1 and len(population[x+1]) > y:
        if population[x+1][y] <= strength and population[x+1][y] != -1:
            d = (x+1, y)
            neighbors.append(d)
    return neighbors
    
p1 = [[6, 7,4], [6, 3, 1, 4, 7], [0, 2, 4, 1, 3, 2], [8, 1, 1, 4, 9], [1,2,3,2,2,2,2,2,6,2,2,2,],[3]]
for a in p1:
    print a
print 
p2 = answer(p1,4,11,6)
for a in p2:
    print a
    