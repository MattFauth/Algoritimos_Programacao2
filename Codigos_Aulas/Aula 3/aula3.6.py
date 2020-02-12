'''
a=''
if a:
    print(a)
b=0
if b:
    print(b)
c=[]
if c:
    print(c)
d= None
if d:
    print(d)
e = False
if e:
    print(e)
'''
'''
string ='abc'
print(len(string))
print(len('abc'))
print(string[0])
print('abc'[0])
print('abc'[len('ab')])
'''
RG = '123.456'
divideRG = RG.split('.')#O que tiver aqui é usado para dividir a string em uma lista
print(RG)
print(divideRG)

lista=['A','B','C']
temp='abc'
novo=temp.join(lista)#Junta a string; pode também juntar strings com listas
print(novo)
novoRG='.'.join(divideRG)
print(novoRG)

palavra=['P','R','O','V','A']
novaPalavra=''.join(palavra)
print(novaPalavra)
