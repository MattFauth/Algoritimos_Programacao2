#ainda sobre string

palavra = "orangotango"
print('Quantidade de \'o\':',palavra.count('o'))
print('Quantidade de \'an\':',palavra.count('an'))
print('**********************')
frase = input('Digite uma frase:')
if frase.islower():
    print('A frase está toda em minúsculas')
elif frase.isupper():
    print('A frase está toda em maiúsculas')
elif frase.istitle():
    print('A frase tem somente as primeiras letras em maiúculas')

print('**********************')
texto = input('Digite um texto:')
if texto.isalnum():
    print('O texto contém somente letras ou números')
else:
    print('O texto contém outros símbolos')
if texto.isalpha():
    print('O texto contém somente letras')
elif texto.isdigit():
    print('O texto contém somente números')
elif texto.isalnum():
    print('O texto contém somente letras ou números')
if texto.startswith('a'):
    print('O texto começa com a')
if texto.endswith('o'): #Pode pesquisar palavras inteiras
    print('O texto termina com o')
if 'bc' in texto:
    print('TExto contém bc')
print('**********************')


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
