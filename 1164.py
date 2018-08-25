#coding: utf-8

n = int(raw_input())
lista = []

for i in range(n):
	numero = int(raw_input())
	lista.append(numero)

for item in range(len(lista)):
	soma = 0
	for i in range(1,lista[item]):
		if lista[item] % i == 0:
			soma += i
	if soma == lista[item]:
		print "%d eh perfeito" %lista[item]
	else:
		print "%d nao eh perfeito" %lista[item]

