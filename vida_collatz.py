# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Vida collatz

numeros = []

n = int(raw_input())

numeros.append(n)

while True:
	if n % 2 == 0:
		n = n / 2
		numeros.append(n)
	else:
		n = 3 * n + 1
		numeros.append(n)
	if n == 1:
		break

print len(numeros)
	
