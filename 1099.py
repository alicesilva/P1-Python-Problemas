#coding: utf-8
N = int(raw_input())
lista_soma = []
soma = 0

for i in range(N):
	numeros = raw_input()
	dados = numeros.split()
	x = int(dados[0])
	y = int(dados[1])
	for item in range(x+1,y,1):
		if item % 2 != 0:
			soma += item
	lista_soma.append(soma)
	
print lista_soma
