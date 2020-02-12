def leArquivo(nome):
    arq=open(nome,'r')
    conteudo=arq.read()
    arq.close
    return conteudo
def separaLinhas(conteudo):
    return conteudo.split('\n')
def separaDados(linha):
    return linha.split(';')
def escreveArquivo(nome,linha):
    arq=open(nome,linha)
    arq.write(linha)
    arq.close()
