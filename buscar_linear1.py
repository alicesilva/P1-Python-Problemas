# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Busca linear

def busca(seq, valor):
	for i in range(len(seq)):
		if valor == seq[i]:
			return i
			break
	if valor not in seq:
		return -1
