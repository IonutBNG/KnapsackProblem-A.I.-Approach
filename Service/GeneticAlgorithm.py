import random
import matplotlib.pyplot as matplot


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


# returns the fitness of one individual
# in this case: value if the weight is lower than the capacity of the knapsack
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
def mutation(individual):
    pos = random.randint(0, len(individual) - 1)
    if individual[pos] == 0:
        individual[pos] = 1
    else:
        individual[pos] = 0
    return individual


# selects 2 individuals from the population and returns the one with better fitness
def selection(population, vv, wv, cap):
    ind1 = random.randint(0, len(population) - 1)
    ind2 = random.randint(0, len(population) - 1)

    if fitness(population[ind1], vv, wv, cap) > fitness(population[ind2], vv, wv, cap):
        return population[ind1]
    else:
        return population[ind2]


def chooseParents(population):
    eligibility = 0.33
    luck = 0.1

    elite = int(len(population) * eligibility)
    unlucky = population[elite:]
    lucky = population[:elite]

    for ul in unlucky:
        if luck > random.random():
            lucky.append(ul)

    return lucky


# the new population will be formed out of the chosen parents and the newly generated children
def newPopulation(population, vv, wv, cap):
    mutationChance = 0.4
    parents = chooseParents(population)
    reqChildren = len(population) - len(parents)
    children = []
    while reqChildren > len(children):
        male = selection(parents, vv, wv, cap)
        female = selection(parents, vv, wv, cap)
        child = crossover(male, female)
        if mutationChance > random.random():
            child = mutation(child)
        if fitness(child, vv, wv, cap) > 0:
            children.append(child)
    children.extend(parents)
    return children


# crossover process represents the creation of a new child
# process: according to a certain "ratio" the child will receive male's first part and female's ending part
def crossover(male, female):
    ratio = 0.3
    coLen = int(len(male) * ratio)
    child = male[:coLen] + female[coLen:]

    return child


def average(population, vv, wv, cap):
    sum = 0
    for p in population:
        sum += fitness(p, vv, wv, cap)
    return sum / len(population)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# First step -> generating the population
# Second step -> sort the population by its fitness
# Third step -> selecting the best individual(the first one) if he is 'better' than the last one
# Fourth step -> create a new population
# Fifth step -> repeat from Second step again and again until all the generations pass
# Return the best individual that ever existed
def GASolution(genNo, popNo, n, vv, wv, cap):
    population = populationGeneration(n, popNo, vv, wv, cap)
    bestInd = [0] * n
    y = []
    x = []
    for i in range(genNo):
        population = sorted(population, reverse=True, key=lambda x: fitness(x, vv, wv, cap))
        if fitness(bestInd, vv, wv, cap) < fitness(population[0], vv, wv, cap):
            bestInd = population[0].copy()
        population = newPopulation(population, vv, wv, cap)
        x.append([fitness(bestInd, vv, wv, cap), fitness(population[len(population) - 1], vv, wv, cap)])
        y.append(i)
    matplot.ylabel("Average fitness")
    matplot.xlabel("Generation")

    matplot.plot(y, x)
    matplot.show()
    return bestInd
