def teste1(a,b):
    print('a =', a)
    print('b =', b)
def teste2(a,b,c = 'oi'):
    print('a =', a)
    print('b =', b)
    print('c =', c)
def teste3(a, b = 'ola', c = 'oi'):
    print('a =', a)
    print('b =', b)
    print('c =', c)
def teste4(a,b, *c):
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('print de if c')
    if c:
        print('c =', end = ' ')
        for i in c:
            print(i, ' ', end='-') #qual o valor default de end? r: Pular linha(\n)
        print( )
