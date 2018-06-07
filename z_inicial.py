# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Z inicial

def z_inicial(lista):
	cont = 0
	for i in range(len(lista)):
		if lista[i][0] == "z" or lista[i][0] == "Z":
			cont += 1
	
	return cont

palavras = raw_input()
lista = palavras.split()
print z_inicial(lista)

