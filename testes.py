def cria_arq(lista):
    arq=open('ArqListas.txt','a')

    arq.write("~")
    arq.write(lista[0])
    arq.write("\n")
    arq.write(str(lista[1]))
    arq.write("\n")
    for index in range(len(lista[2])):
        arq.write(lista[2][index])
        arq.write(";")
    arq.write("\n")
    for index in range(len(lista[3])):
        arq.write(str(lista[3][index]))
        arq.write(";")
    arq.write("\n")
    
#    arq.write(str(lista[1]))
 #   arq.write("\n")

    return
        
listaTeste=['Daniel Coelho',4,['Arroz','Feijão'],[7,5]]
listaTeste2=['Pedro Antônio Tibau Velozo',5,['Arroz','Macarrão','Maçã','Uva','Carne'],[3,4,5,6,6]]
cria_arq(listaTeste)    
cria_arq(listaTeste2)




#lista = ['nome',5,['c', 'e'],[1, 2]]
    
'''
def cria_arq(lista):
    arq=open('ArqListas.txt','a')

    arq.write("~", lista[0],"\n")
    arq.write("~", lista[0],"\n")
    arq.write("~", lista[0],"\n")
    arq.write(lista[1], "\n")
    for index in range(len(lista[2])):
        arq.write(lista[2][index],";")
    arq.write("\n")
    for index in range(len(lista[3])):
        arq.write(lista[3][index],";")
    arq.write("\n")
    
    arq.write(lista[1], "\n")
'''
