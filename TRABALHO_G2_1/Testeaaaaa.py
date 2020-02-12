def leArquivo(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    linha=conteudo.replace('";"',';')
    conteudo=linha.replace('"','')
    arq.close
    return conteudo

def separaLinhas(conteudo):
    conteudo=conteudo.split('\n')
    conteudo1 = []
    for i in conteudo:
        conteudo1.append(i.split(';'))
    return conteudo1


def achaPartido(Separa):
    separavotos=[]
    nomePartido=input('Digite o nome do partido:')
    for Partido in Separa[11]:
        if nomePartido == Separa[11]:
            voto=Separa[11]
            separavotos.append(voto)
    return separavotos


#MAIN
arq=leArquivo('aaaa.txt')
print(arq)
Separa=separaLinhas(arq)
print(Separa)
Partido=achaPartido(Separa)
print(Partido)
