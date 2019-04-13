from Service import GeneticAlgorithm, HillClimbing


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Get&set the input >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def readFromFile():
    inputFile = open("InputResources/input.txt", "r")

    global n
    # n -> number of objects
    n = int(inputFile.readline())

    global wv
    # wv -> weights vector
    wv = [int(entity) for entity in inputFile.readline().split(",")]

    global vv
    # vv -> value vector
    vv = [int(entity) for entity in inputFile.readline().split(",")]

    global cap
    # cap -> backpack capacity
    cap = int(inputFile.readline())
    inputFile.close()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> Output >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def writeToFile(solution, fileName):
    outputFile = open(fileName, "w")

    # First line -> number of selected items
    outputFile.write(str(checkTotals(solution, solution)) + "\n")

    # Second line -> binary list representing the selected items: 1 -> selected; 0 -> not selected
    outputFile.write(",".join(map(str, solution)) + "\n")

    # Third line -> values of the selected items: value 'v' if the item was selected, 0 otherwise
    if solution[0] == 1:
        outputFile.write(str(vv[0]))
    else:
        outputFile.write("0")

    for i in range(1, n):
        if solution[i] == 1:
            outputFile.write("," + str(vv[i]))
        else:
            outputFile.write(",0")
    outputFile.write("\n")

    # Fourth line -> total value of the selected items
    outputFile.write(str(checkTotals(solution, vv)))
    outputFile.close()


# >>>>>>>>>>>>>>>>>>>>>>>>> Additional methods >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Calculate the max weight of the items
def checkMaxWeight():
    s = 0
    for i in range(len(wv)):
        s += wv[i]

    return s


# Calculate sum of valid items from v
# One item is valid if on the same position in binList is 1
def checkTotals(binList, v):
    sum = 0
    for i in range(len(binList)):
        if binList[i] == 1:
            sum += v[i]
    return sum


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def main():
    # read the input
    readFromFile()
    if cap == 0:
        allItmSolution = [0 for i in range(n)]
        writeToFile(allItmSolution, "output.txt")
    else:
        if checkMaxWeight() > cap:
            print("Commands: \n 1 Genetic Algorithm \n 2 Hill Climbing \n")
            command = input("Give command: ")
            if command == "1":
                # genetic algorithm solution
                generations = int(input("Number of generations: "))
                individuals = int(input("Number of individuals: "))
                gaSolution = GeneticAlgorithm.GASolution(generations, individuals, n, vv, wv, cap)
                writeToFile(gaSolution, "Output/gaOutput.txt")
            elif command == "2":
                # hill climbing solution
                generations = int(input("Number of generations: "))
                individuals = int(input("Number of individuals: "))
                hcSolution = HillClimbing.HillClimbing(generations, individuals, n, vv, wv, cap)
                writeToFile(hcSolution, "Output/hcOutput.txt")

        else:
            # weight.total <=  capacity
            allItmSolution = [1 for i in range(n)]
            writeToFile(allItmSolution, "output.txt")


main()
