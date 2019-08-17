##  IMPORTS  ##

import erro1
import enum

##  TYPEDEFS AND ENUMS  ##


class Foods(enum.Enum):

    Refrigerante = 1
    Cerveja = 2
    Biscoito = 3


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


##  TESTES

#errArray = [None]
#errArray2 = None
#print(erro1.not_null(None))
#print(erro1.not_null([None]))
#obj1 = User("Pedro", 4, ["leite", "feijao"], [1, 2])
#print(obj1.userName, obj1.memberAmount, obj1.foodArray, obj1.foodAmount)
#print(Foods.Refrigerante.name)
#print(Communication.check_in([None,1]))
listaTeste=['Daniel Coelho', 4, ['Arroz','Feijao'], [7,5]]
listaTeste2=['Pedro Antonio Tibau Velozo', 5, ['Arroz','Macarrao','Maca','Uva','Carne'], [3,4,5,6,6]]
Communication.escrever_arq(listaTeste)
Communication.escrever_arq(listaTeste2)
print(Communication.ler_arq("ArqListas.txt"))
