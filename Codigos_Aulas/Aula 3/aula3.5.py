palavra = ['A','B','C','D','E']
'''
letra = palavra[3] #\n conta como um caracter
print(letra)
print(palavra[5])
comprimento = len(palavra)
print(comprimento)
ultima = palavra[comprimento-1]
print(ultima)
'''

i= 0
while i < len(palavra):
    print(palavra[i])
    i+=1
print('**********')
i = len(palavra)-1
while i >= 0:
    print(palavra[i])
    i-=1
print('***********')
for letra in palavra:
    print(letra, end='.')
print()
print('***********')
for i in range(len(palavra)):
    print(palavra[i])
print('***********')
for i in range(len(palavra)-1,-1,-1):
    print(palavra[i])
print('***********')
for i in range(10,1,-2):
    print(i)
