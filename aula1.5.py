'''
def soma(a,b):
    return a+b
print(id(soma(3,2)))
print(id(5))
print(id(soma))
'''
def teste(*args):
    print(args)
    'for i in args:'
#main
teste(1,'a',2,'fabiano') #resultado é uma tupla, que é imutável
