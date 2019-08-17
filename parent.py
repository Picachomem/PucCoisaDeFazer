##  IMPORTS  ##

import erro1
import enum

##  TYPEDEFS AND ENUMS  ##

'''
class Foods(enum.Enum):

    Refrigerante = 1
    Cerveja = 2
    Biscoito = 3
'''

##  BEGIN MAIN  ##

##  SHOULD BE COMPLETELY STATIC  ##
class Communication:

    def check_in(array):
        if (erro1.not_null(array) != 0):
            return erro1.not_null(array)
        pass

    def ler_arq(nomeArq):

        result = list()
        currentArray = list()
        currentLine = ""
        listComida = list()
        auxArray = list()
        count = 0

        arq = open(nomeArq, "r")
        linesAmount = len(arq.readlines())
        arq.close()

        arq = open(nomeArq, "r")
        for index in range(linesAmount):

            count += 1
            currentLine = arq.readline()

            if (currentLine[0] == "~"):
                currentArray.append(currentLine[1:len(currentLine) - 1])
                count = 0

            if (count == 1):
                currentArray.append(int(currentLine))
            if (count == 2):
                currentArray.append(currentLine.split())

            if (count == 3):
                auxArray.clear()
                for index2 in range(len(currentLine.split())):
                    auxArray.append(int(currentLine.split()[index2]))
                currentArray.append(auxArray.copy())

                result.append(currentArray.copy())
                currentArray.clear()

        return result

    def escrever_arq(array):

        arq = open('ArqListas.txt', 'a')

        arq.seek(0)

        arq.write("~")
        arq.write(array[0])
        arq.write("\n")
        arq.write(str(array[1]))
        arq.write("\n")
        for index in range(len(array[2])):
            arq.write(array[2][index])
            arq.write(" ")
        arq.write("\n")
        for index in range(len(array[3])):
            arq.write(str(array[3][index]))
            arq.write(" ")
        arq.write("\n")

        return 0


class User:

    def __init__(self, userName, memberAmount, foodArray, foodAmount):
        self.userName = userName
        self.memberAmount = memberAmount
        self.foodArray = foodArray
        self.foodAmount = foodAmount
#    frequency
    pass


class AverageCalculator:

    def set_totals(self):

        rawData = Communication.ler_arq("ArqListas.txt")
        rawFoods = read_foods()
        rawSums = list()
        rawPeople = list()

        for index in range(len(rawFoods)):

            rawSums.append(0)
            rawPeople.append(0)

            for index2 in range(len(rawData)):

                for index3 in range(len(rawData[index2][2])):

                    if (rawData[index2][2][index3] == rawFoods[index]):
                        rawSums[index] += rawData[index2][3][index3]
                        rawPeople[index] += 1

        return [rawSums, rawPeople]

    def set_average(self, sumArray, peopleArray):

        result = list()

        for index in range(len(sumArray)):
            if (peopleArray[index] != 0):
                result.append(sumArray[index]/peopleArray[index])

        return result



##  AUXILIARY FUNCTIONS  ##


def read_foods():

    listaVazia = list()
    arq = open('foods.txt', 'r')
    linha = arq.readline()

    while linha != '':
        listaVazia.append(linha)
        linha = arq.readline()

    for index in range(len(listaVazia)):
        if listaVazia[index][-1] == '\n':
            listaVazia[index] = listaVazia[index][0:-1]

    return listaVazia

##  TESTES


print(Communication.ler_arq("ArqListas.txt"))

AverageObj = AverageCalculator()

totals = AverageObj.set_totals()

print(totals[0])
print(totals[1])

print(AverageObj.set_average(totals[0], totals[1]))
