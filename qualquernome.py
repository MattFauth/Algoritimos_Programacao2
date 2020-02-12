'''
#ORIGNAL
import func #importa todas as funções, tem que usar o nome do módulo
a = 10
b= 5
print('teste1') #print para organização
func.teste1(b, a)
print('teste 2 com 3 argumentos')
func.teste2(1,5,10)
print('teste 2 com 2 argumentos')
func.teste2(6,12)

'''
from func import * #importa somente uma função do módulo *=all
#import func #
a = 10
b= 5
print('teste1') #print para organização
teste1(4,5)
print('teste 2 com 3 argumentos')
teste2(1,5,10)
print('teste 2 com 2 argumentos')
teste2(6,12)
print('teste 3 com 3 argumentos')
teste3('a','b','c')
print('teste 3 com 2 argumentos')
teste3('x','y')
print('teste3 com 1 argumento')
teste3('k')
print('Teste 4 com 3 argumentos')
teste4(5,6,7)
print('Teste 4 com 2 argumentos')
teste4(8,9)
print('Teste 4 com 5 argumentos')
teste4(10,20,30,40,50)
print('(FIM)')
