import random


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Generate >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def individualsGeneration(n, vv, wv, cap):
    individual = [random.randint(0, 1) for i in range(0, n)]
    while fitness(individual, vv, wv, cap) == 0:
        individual = [random.randint(0, 1) for i in range(0, n)]
    return individual


def populationGeneration(n, popNo, vv, wv, cap):
    population = [individualsGeneration(n, vv, wv, cap) for i in range(0, popNo)]
    return population


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Fitness & mutation >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def fitness(individual, vv, wv, cap):
    value = 0
    weight = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            value += vv[i]
            weight += wv[i]

    if weight > cap:
        return 0
    else:
        return value


# random negation
def extremeMutation(individual, times):
    for i in range(0, times):
        pos = random.randint(0, len(individual) - 1)
        if individual[pos] == 0:
            individual[pos] = 1
        else:
            individual[pos] = 0

        # while individual[pos1] == individual[pos2]:
        pos1 = random.randint(0, len(individual) - 1)
        pos2 = random.randint(0, len(individual) - 1)

        aux = individual[pos1]
        individual[pos1] = individual[pos2]
        individual[pos2] = aux

    return individual


# random negation
def mutation(individual):
    pos = random.randint(0, len(individual) - 1)
    if individual[pos] == 0:
        individual[pos] = 1
    else:
        individual[pos] = 0
    return individual


# Calculate sum of valid items from v
# One item is valid if on the same position in binList is 1
def checkTotals(binList, v):
    sum = 0
    for i in range(len(binList)):
        if binList[i] == 1:
            sum += v[i]
    return sum


def newPopulation(population, totalInd, survivors, vv, wv, cap):
    newBreed = []

    for ind in population:
        indBreed = []
        for i in range(0, totalInd):
            if cap - checkTotals(wv, ind) < cap * 0.4:
                newB = mutation(ind)
                if fitness(newB, vv, wv, cap) > 0:
                    indBreed.append(newB)
            else:
                newB = extremeMutation(ind, 3)
                if fitness(newB, vv, wv, cap) > 0:
                    indBreed.append(newB)
        indBreed = sorted(indBreed, reverse=True, key=lambda x: fitness(x, vv, wv, cap))
        if len(indBreed) > survivors:
            newBreed.extend(indBreed[:survivors])
        else:
            newBreed.extend(indBreed)
    return newBreed


def average(population, vv, wv, cap):
    sum = 0
    for p in population:
        sum += fitness(p, vv, wv, cap)
    return sum / len(population)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>       >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def HillClimbing(genNo, popNo, n, vv, wv, cap):
    population = populationGeneration(n, popNo, vv, wv, cap)
    bestInd = [0] * n
    totalInd = 10
    survivors = 4
    maxPop = 500
    mortalityRate = 0.73

    for i in range(genNo):
        population = sorted(population, reverse=True, key=lambda x: fitness(x, vv, wv, cap))
        if i > int(genNo * 0.85):
            for j in range(0, int(0.6 * len(population))):
                randV = random.randint(0, len(population) - 1)
                population[randV] = extremeMutation(population[randV], 10)

        if len(population) > maxPop:
            population = population[:int(maxPop * mortalityRate)]
        if fitness(bestInd, vv, wv, cap) < fitness(population[0], vv, wv, cap):
            bestInd = population[0].copy()

        population = newPopulation(population, totalInd, survivors, vv, wv, cap)
    return bestInd
