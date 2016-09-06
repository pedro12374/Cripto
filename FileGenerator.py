import Variables
import AlfaCrip

teste = open('Testes.txt', 'w')

teste.write(str(Variables.Day) + "\n")
teste.write(str(Variables.Month) + "\n")
teste.write(str(Variables.Year) + "\n")
teste.write(str(Variables.Hora) + "\n")
teste.write(str(Variables.Min) + "\n")
teste.write(str(Variables.Sec) + "\n")

inputTxt = raw_input("Manda a vdd brow: ")

word_list = []
for item in inputTxt:
    for word in item:
        word_list.append(word)

while " " in word_list:
    word_list.remove(" ")

convertLetNum = []
ListaDicL = AlfaCrip.listaDicL

def convertToL(Letra):

    convertLetNum = ListaDicL[Letra]
    return convertLetNum



for i in word_list:
    pp = []
    pp.append(convertToL(i))
    print i


'''
for i in range(len(vdd)):
    texto = str(vdd[i] + "\n")
    teste.write(texto)
'''


teste.close()
print pp
print ListaDicL["m"]