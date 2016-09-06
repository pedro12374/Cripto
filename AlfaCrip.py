import string

alfa = list(string.ascii_lowercase)
lista = []


listaDicL = {} #Transforma uma letra em um numero correspondente
for i in range(len(alfa)):
    lista.insert(i,[alfa[i],i])
    lt = {alfa[i]:i}
    listaDicL.update(lt)

def AlfaCripL (L):
    l = listaDicL[L]
    return l


listaDicN = {} #Transforma um numero na letra correspondente
for i in range(len(alfa)):
    lista.insert(i,[alfa[i],i])
    lt = {i:alfa[i]}
    listaDicN.update(lt)

def alfaCripN (L):
    l = listaDicN[L]
    return l



