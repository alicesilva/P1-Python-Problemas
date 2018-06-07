# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Sequência caras

def sequencia_caras(lancamentos):
	cont = 0
	maior = 0
	for i in range(len(lancamentos)):
		if lancamentos[i] == 1:
			cont += 1
		else:
			cont = 0
		if cont > maior:
			maior = cont
	return maior
