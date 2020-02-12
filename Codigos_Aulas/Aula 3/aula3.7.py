arq=open('teste.txt','r')
conteudo1=arq.read()
arq.close()
arq=open('teste.txt','r')
conteudo2=arq.readlines()

print(conteudo1)
print(conteudo2)

arq.close()

conteudo3=conteudo1.split('\n')
print(conteudo3)
arq.close()

for i in conteudo3:
    print(i)
print('*********')
for i in conteudo2:
    print(i)
print('*********')
for i in conteudo1:
    print(i)
