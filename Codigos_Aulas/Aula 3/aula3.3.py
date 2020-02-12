arq=open('temp.txt', 'r')#r = read
conteudo = arq.readlines()
print(conteudo)
'''
conteudo2 = arq.read()
print(conteudo2)
'''
arq.close()
