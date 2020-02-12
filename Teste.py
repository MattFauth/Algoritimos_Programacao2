def leArquivo(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    arq.close
    return conteudo

def separaLinhas(conteudo):
    conteudo=conteudo.split('\n')
    conteudo1 = []
    for i in conteudo:
        conteudo1.append(i.split(';'))
    return conteudo1

'''def achaCidade(arqseparado):
    codigocidade=input('Digite o codigo da cidade:')
    for teste in arqseparado:
        codCidade = teste[13]
    return codCidade'''

#MAIN
arq=leArquivo('TRE.txt')
arqseparado=separaLinhas(arq)
print(arqseparado)
#Seleciona Cidade e cargos
'''
buscaCidade=achaCidade(arqseparado)
print(buscaCidade)'''
'''buscaCargo=achacargo(input('Digite qual cargo quer ver os numeros de votos:'))
arq.close()
'''
