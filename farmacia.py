def leArquivo(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    arq.close
    return conteudo

def separaLinhas(conteudo):
    conteudo=conteudo.split('\n')
    conteudo1 = []
    for i in conteudo:
        conteudo1.append(i.split(','))
    return conteudo1

def pegaPreco(linha):
    montar= str(linha[2]) +'.' + str(linha[3])
    montar=montar.replace('"', '')
    return float(montar)

def pegaDesc(i):
    print(i[1])
    return i[1]
def pegaCod(i):
    print(i[0])
    return i[0]

def quantTotalVendas(listaVendas,codigo):
    soma =0
    for i in listaVendas:
        if i[0]==codigo:
            soma= soma+int(i[1])
    return soma
def quantTotalEstoque(listaEstoque,codigo):
    for i in listaEstoque:
        if i[0]==codigo:return int(i[1])
#######################################################
conteudoDesc = leArquivo('descricao.csv')
listaDesc = separaLinhas(conteudoDesc)

conteudoVendas = leArquivo('vendas.csv')
listaVendas = separaLinhas(conteudoVendas)

conteudoEstoque = leArquivo('estoque.csv')
listaEstoque = separaLinhas(conteudoEstoque)

arq = open('relatorio.csv','w')
   
arq.write('Codigo;Descricao;Total em Estoque; Total de Vendas; Preco Unitario; Valor Total; Resta em Estoque\n')

for i in listaDesc:
    codigo = pegaCod(i)
    descricao = pegaDesc(i)
    preco=pegaPreco(i)
    totalVendas=quantTotalVendas(listaVendas,codigo)
    totalEstoque=quantTotalEstoque(listaEstoque,codigo)
    valorTotal = totalVendas*preco
    arq.write(codigo+','+descricao+','+str(totalEstoque)+','+str(totalVendas)+','+str(preco)\
              +','+str(valorTotal)+','+str(totalEstoque-totalVendas)+'\n')
arq.close()
#######################################################


