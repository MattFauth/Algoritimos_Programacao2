
print('Faça uma função que receba uma string e uma letra como argumento e imprima no índice de todas as posições em que letra aparece na palavra.')
def indices(string, letra):
    i= string.find(letra)
    while i!=-1:
        print(i)
        i = string.find(letra, i+1)
print('Faça uma função que receba duas strings como argumento e retorne True se a segunda string estiver contida na primeira e False caso contrário')
def contem(string1, string2): #def contem(string1, string2):
    if string2 in string1:      #return string1.find(string2)!=-1
        return print('True')
    else:
        return print('False')


print('Faça uma função que receba o nome(completo) de um arquivo e uma palavra como argumentos e retorna TRUE se a palavra estiver no arquivo e FALSE caso contrário')
def arquivoContem(arquivo, palavra):
    arquivo = arq = open('texto.txt', 'r')
    palavra = palavra
    if palavra in arquivo:
        return print('True')
    else:
        return print('False')
    arq.close()
