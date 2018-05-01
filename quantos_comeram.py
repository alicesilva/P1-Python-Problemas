# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Quantos comeram

def quantos_comeram(N,fila):
	subtracao = N
	soma = 0
	for i in range(len(fila)):
		subtracao -= int(fila[i])
		if subtracao >= 0:
			soma += int(fila[i])
		
	return soma

assert quantos_comeram(10, [4, 3]) == 7
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5
assert quantos_comeram(10, [5, 6]) == 5
assert quantos_comeram(20, [5, 6, 1, 2, 4, 30]) == 18
