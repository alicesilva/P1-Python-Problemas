# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Soma simétricos

def soma_simetricos(valores):
	somas = []
	for item in range(len(valores)/2):
		for i in range(len(valores)):
			soma = valores[item] + valores[(len(valores)-1-item)]
		somas.append(soma)
	if len(valores) % 2 != 0:
		somas.append(valores[len(valores) / 2])

	return somas
