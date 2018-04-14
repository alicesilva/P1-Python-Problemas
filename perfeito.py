# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Número perfeito
soma = 0
numero = int(raw_input())
for i in range(1,numero,1):
	if numero % i == 0:
		soma += i

if soma == numero:
	print "%d é um número perfeito." %numero
else:
	print "%d não é um número perfeito." %numero
