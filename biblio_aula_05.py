def NomeAbnt(string):
    x = string.split(' ')
    abrev = []
    if sobname(x[-1]):
       abrev = x[len(x)-1].upper() + ','
       for i in x:
           if (conects(i) and i!=x[-1]):
               abrev+=i[0].upper()+"."
    else:
       abrev = x[len(x)-2].upper()+" "+x[len(x)-1].upper() + ','
       for i in x:
           if (conects(i) and i!=x[-1] and i!=x[-2]):
               abrev+=i[0].upper()+"."
    return abrev
    
def conects(string):
    var = ['da','do','de','das','dos','e']
    for i in var:
        if string == i:return False
    return True
def sobname(string):
    var = ['Neto','sobrinho','Junior','Filho']
    for i in var:
        if string == i: return False
    return True

