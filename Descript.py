teste = open('Testes.txt', 'r')

f = teste.readlines()
f = map(lambda s: s.strip(), f)

finalConvertString = []
for i in f:
    m = i.replace(' ', '')
    finalConvertString.append(m)

while '' in finalConvertString:
    finalConvertString.remove('')

finalConvertString = [int(x) for x in finalConvertString]

print finalConvertString