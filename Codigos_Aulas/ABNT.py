from math import *
from string import *
def nomeABNT(string1, string2):
    artigos = [da,do,de,das,dos,e]
    sufixo = [Filho,Neto,Sobrinho,Junior]
    if string1 == ' ':
        nome = input('Digite seu nome completo:')
        ultimo_espaco = nome.rfind(' ')
        primeiro_espaco = nome.find(' ')
        ultima_palavra = nome[ultimo_espaco+1:]
        primeira_palavra = nome[:primeiro_espaco]
        ultima_palavra = ultima_palavra.upper()
        primeira_palavra = primeira_palavra.capitalize()
        abnt = ultima_palavra + ', ' + primeira_palavra[0]
        while primeiro_espaco != ultimo_espaco:
            inicial = nome[primeiro_espaco+1]
            inicial = inicial.upper()
            abnt = abnt + '.' + inicial + '.'
            primeiro_espaco = nome.find(' ', primeiro_espaco+1)
        print ('Nome padrão ABNT:', abnt)
    else:
        print('Erro')
