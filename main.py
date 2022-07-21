#testes básicos e variáveis
#a = 16
#b = 20
#c = a + b
#print(c)

import testOper.operations
import testeClasse
import testsJson

#try:
a = 1
b = 2
c = testOper.operations.soma(a, b)
print(c)

d = testeClasse.TesteClassesPy()
f = d.retornarMensagem(1)
print(f)

z = testsJson.stringToObject()
print(z)

valueInput = input('Digite o valor do parâmetro procurado')

resultFindParameter = testsJson.findParameterJson(valueInput)
print(resultFindParameter)

#except:
    #print('Erro')

