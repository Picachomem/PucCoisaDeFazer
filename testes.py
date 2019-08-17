def cria_arq(lista):

    arq = open('ArqListas.txt','r')
    
    arq=open('ArqListas.txt','a')

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
    

    return
'''
listaTeste=['Daniel Coelho',4,['Arroz','Feijão'],[7,5]]
listaTeste2=['Pedro Antônio Tibau Velozo',5,['Arroz','Macarrão','Maçã','Uva','Carne'],[3,4,5,6,6]]
cria_arq(listaTeste)    
cria_arq(listaTeste2)
'''

def ler_arq():

    result = list()
    currentArray = list()
    currentLine = ""
    listComida = list()

    arq = open("ArqListas", "r")
    linesAmount = len(arq.readlines())
    arq.close()

    arq = open("ArqListas", "r")
    for index in range(linesAmount):

        currentLine = arq.readline()

        if (currentLine[0] == "~"):
            result.append(currentArray)
            currentArray.clear()
            currentArray = list()
            currentArray.append(currentLine[1:len(currentLine)])

        currentLine = int(arq.readline())



        





    
