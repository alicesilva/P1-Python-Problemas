#coding: utf-8
n = int(raw_input())

soma = 0
numero = []

for i in range(n):
	numeros = int(raw_input())
	if 0 <= numeros <= 1000:
		soma += numeros
		numero.append(numeros)

menor = 0
maior = 0

if  numero != []:
	maior = numero[0]
	menor = numero[0]
	for i in range(len(numero)):
		if numero[i] > maior:
			maior = numero[i]
		if numero[i] < menor: 
			menor = numero[i]

print menor
print maior
print soma
