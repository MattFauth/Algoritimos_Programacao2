def funcao1(x): #só aparece quando chamado
    print('x antes de mudar:', x)
    print('id(x) antes de mudar:', id(x))
    x = 100
    print('x apos mudar:', x)
    print('id(x) depois de mudar:', id(x))
#main
a = 10 #começa aqui
print('a antes da função1:', a)
print('id(a) antes da funcao1:', id(a))
funcao1(a) #Para e volta para o def, a vira x
print('a depois da funcao1:', a) #volta pra ca normalmente, a continua 10
print('id(a) apos a funcao1:', id(a))
funcao1(7) #aceita qualquer coisa que não altere a função
print('*************')
def funcao2(a): #só aparece quando chamado
    print('a antes de mudar:', a)
    print('id(a) antes de mudar:', id(a))
    a = 200
    print('a apos mudar:', a)
    print('id(a) depois de mudar:', id(a))
#main
a = 10
print('a antes da função2:', a)
print('id(a) antes da funcao2:', id(a))
funcao2(a) 
print('a depois da funcao2:', a) #a de fora da função não tem nada a ver com o de dentro
print('id(a) apos a funcao2:', id(a))
