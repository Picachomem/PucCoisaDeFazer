def escrever_arq(lista):

    arq=open('ArqListas.txt', 'a')

    arq.seek(0)

    arq.write("~")
    arq.write(lista[0])
    arq.write("\n")
    arq.write(str(lista[1]))
    arq.write("\n")
    for index in range(len(lista[2])):
        arq.write(lista[2][index])
        arq.write(" ")
    arq.write("\n")
    for index in range(len(lista[3])):
        arq.write(str(lista[3][index]))
        arq.write(" ")
    arq.write("\n")

    return 0

listaTeste=['Daniel Coelho', 4, ['Arroz','Feijao'], [7,5]]
listaTeste2=['Pedro Antonio Tibau Velozo', 5, ['Arroz','Macarrao','Maca','Uva','Carne'], [3,4,5,6,6]]
escrever_arq(listaTeste)
escrever_arq(listaTeste2)


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

def read_foods():

    listaVazia=list()
    arq=open('foods.txt','r')
    linha=arq.readline()
    while linha != '':
        listaVazia.append(linha)
        linha=arq.readline()

    for index in range(len(listaVazia)):
        if listaVazia[index][-1] == '\n':
            listaVazia[index] = listaVazia[index][0:-1]

    print(listaVazia)
    return

read_foods()



print(ler_arq("ArqListas.txt"))

        





    
