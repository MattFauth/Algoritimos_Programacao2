from trab1 import *
print("Função de achar:")
palavra1= input("Digite uma palavra:")
letra= input("Digite uma letra:")
print('Indices de',letra,':')
indices(palavra1, letra)
print('**********')
print("Função de ver e contém:")
string1 = input("Digite uma palavra:")
string2 = input("Digite um série de letras:")
string3 = input("Algo que não exista na palavra:")
contem(string1, string2)
contem(string1, string3)
print('**********')
arquivoContem('arquivo', 'Alabama')
arquivoContem('arquivo', 'Tucson')
