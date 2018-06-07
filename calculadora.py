# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Calculadora de médias

aritmetica = []
geometrica = []
harmonica = []
while True:
	entrada = raw_input()
	if entrada == "Q":
		break
	dados = entrada.split()

	if dados[0] == "MA":
		for i in range(1,len(dados)):
			aritmetica.append(dados[i])
	elif dados[0] == "MG":
		for i in range(1,len(dados)):
			geometrica.append(dados[i])
	elif dados[0] == "MH":
		for i in range(1,len(dados)):
			harmonica.append(dados[i])

soma = 0.0
for i in range(len(aritmetica)):
	soma += float(aritmetica[i])

mediama = float(soma) / len(aritmetica)

multiplicacao = 1
for i in range(len(geometrica)):
	multiplicacao *= float(geometrica[i])

mediamg = (multiplicacao) ** 1/len(aritmetica)

soma1 = 0
for i in range(len(harmonica)):
	soma1 += 1/float(harmonica[i])

mediamh = len(harmonica) / soma1

print mediama
print mediamg
print mediamh
