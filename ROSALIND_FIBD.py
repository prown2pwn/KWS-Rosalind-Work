numberMonth = 98
lifespan = 20

def mortalrabbit(numberMonth, lifespan):
    pop_array = [{0:1, 1:0, 2:0}, {0:0, 1:1, 2:0}] #base set
    for i in range(2, numberMonth):
        popDict = {}
        sum = 0
        for (key, value) in pop_array[i-1].items(): #age loop to find total population
            if key != 0: #All non new born will produce one baby pair
                sum += value
            if key != 0 and key != lifespan - 1: #all age between 1 to 'death - 1' age per loop
                popDict[key + 1] = value
            if key == 0: #newborn age
                popDict[1] = value
        popDict[0] = sum #all newborn is addedto 'key 0'
        pop_array.append(popDict)
    print(pop_array)
    pop_sum = 0
    for (key, value) in pop_array[numberMonth - 1].items():
        pop_sum += value
    print(pop_sum)
    return pop_sum

mortalrabbit(numberMonth, lifespan)