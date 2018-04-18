# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Sequencia

limite = int(raw_input())

numeros = []

i = 1
numeros.append(i)

soma = 1

while True:
	i *= 2
	soma += i
	if soma >= limite:
		break
	numeros.append(i)

if limite > 1:
	for i in numeros:
		print i
