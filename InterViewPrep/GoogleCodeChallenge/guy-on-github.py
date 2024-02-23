def answer(population, x, y, strength):
    constrain_x = len(population[0])
    constrain_y = len(population)
    places_to_vist = [(x, y,)]
    places_visited = []

    def where_next():
        for item in places_to_vist:
            yield item

    for x, y in where_next():
        if population[y][x] <= strength:
            # print "Position ({}, {}) infected... ({} >= {})".format(x, y, population[y][x], strength)
            places_visited.append((x, y,))
            population[y][x] = -1
            if x - 1 >= 0 and (x-1, y,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x-1, y)
                places_to_vist.append((x-1, y,))
            if x + 1 < constrain_x and (x+1, y,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x+1, y)
                places_to_vist.append((x+1, y,))
            if y - 1 >= 0 and (x, y-1,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x, y-1)
                places_to_vist.append((x, y-1,))
            if y + 1 < constrain_y and (x, y+1,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x, y+1)
                places_to_vist.append((x, y+1,))
        # else:
            # print "Position ({}, {}) NOT infected... ({} < {})".format(x, y, population[y][x], strength)
    return population
#p1 = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
p1 = [[6, 7,4], [6, 3, 1, 4, 7], [0, 2, 4, 1, 3, 2], [8, 1, 1, 4, 9], [1,2,3,2,2,2,2,2,6,2,2,2,],[3]]
for a in p1:
    print a
print 
p2 = answer(p1,0,0,7)
for a in p2:
    print a