#coding: utf-8

n = int(raw_input())

for i in range(n):
	entrada = raw_input()
	dados = entrada.split()
	x = int(dados[0])
	y = int(dados[1])
	if x % 2 == 0:
		soma = 0
		x = x + 1
		for i in range(y):
			soma += x
			x += 2
	else:
		soma = 0
		for i in range(y):
			soma += x
			x += 2

	print soma
