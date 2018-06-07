# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Divisor

def divisor(num, lista):
	cont = 0
	for i in range(len(lista)):
		if lista[i] % num == 0:
			return i
			break
		if lista[i] % num != 0:
			cont += 1
	if cont == len(lista):
		return -1
