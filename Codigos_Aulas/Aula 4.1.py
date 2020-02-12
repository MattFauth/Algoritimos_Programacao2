palavra1='ABRACADABRA'
'''palavra2=['A','B','R','A','C','C','A','D','A','B','R','A']
print(palavra2)
print(palavra1)
palavra2[3]='X'
print(palavra2)
print(palavra1)
print(palavra1.replace('A','X',1))
print(palavra1)
print(palavra1.replace('BR','XY'))
'''
indice = palavra1.find('A')
print('Letra A na posição:', indice)
print('Letra R na posição:', palavra1.find('R'))
if palavra1.find('B') == 1:
    print('A letra B está na posição 1')
print(palavra1.find('BR', 0))
print(palavra1.find('BR', 1))
print(palavra1.find('BR', 2))#A posição é de onde começa a pesquisa
print(palavra1.find('BR', 3))
print('******************')
print(palavra1.find('A', 0,1))
print(palavra1.find('A', 1,3))
print(palavra1.find('A', 1,4))#Os números definem onde é procurado A, não procura na ultima posição
print(palavra1.find('A', 4, 6))
