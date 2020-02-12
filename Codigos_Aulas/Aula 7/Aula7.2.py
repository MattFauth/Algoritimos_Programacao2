lista1=['a','b','c']
lista2= ['d','elefante']
print('Lista antes de append:', lista1)
lista1.append('f')
print('Lista depois do append:', lista1)
print('Tamanho da lista antes do novo append:', len(lista1))
lista1.append(lista2)
print('Tamanho da lista após novo append:', len(lista1))
print(lista1[4][1][4])
lista3 = ['g','h']
lista1.extend(lista3)
print(lista1)
lista4=['A','B']
lista5=['C','D']
lista6=lista4+lista5 #Isso é igual um extend
print(lista6)
lista7=['X','Y','Z']
lista7.insert(-1, 'K')
print(lista7)
#lista7.remove('Y')#Se botar uma letra que não está na lista ele retorna um erro
print(lista7)
#valor = lista7.pop(0)
#print(valor)
print(lista7)
#del lista7[1]
print(lista7)
print('Atendimento:', lista7.pop(0))
print('Novo Atendimento', lista7.pop(0))

lista8=['a','b','c','d', 'a']
#print(lista8.index('b')) #Dá erro se o objeto não estiver na lista
print(lista8.pop(lista8.index('b')))
print(lista8)
print(lista8.count('a'))#Se o objeto não estiver na lista ele retorna 0
print('****LISTA 9****')
lista9=['x','a','c','y','d']
print(lista9)
lista9.sort()
print(lista9)
lista9.reverse()
print(lista9)
print('***LISTA 10***')
lista10=['z','a','w','d']
print(len(lista10))
print(max(lista10))
print(min(lista10))
print(sorted(lista10)) #Sort modifica a lista, Sorted só se atribuir
print(lista10)
lista10 = sorted(lista10)
print(lista10)

lista1 =['a','b','c']
lista2=lista1
print('lista 1 antes do append:', lista1)
print('Lista 2 antes do append:', lista2)
lista1.append('*****')
print('Lista 1 depois do append:', lista1) #Lista 2 está na mesma posição de memória que Lista 1
print('Lista 2 depois do append:', lista2)
lista2[1]='xxxx'
print('lista 1 depois da atribuição:', lista1)
print('Lista 2 depois da atribuição:', lista2)

#Homework: Achar prova antiga e resolver, sem arquivo
