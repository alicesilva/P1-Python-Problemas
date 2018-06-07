# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Conta palavras

def conta_palavras(k, palavras):
	dados = palavras.split(":")
	maior = k
	cont = 0
	for i in range(len(dados)):
		if len(dados[i]) >= maior:
			cont += 1
	return cont


		
