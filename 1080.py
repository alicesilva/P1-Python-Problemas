#coding: utf-8
lista_numero = []

for i in range(100):
	numero = int(raw_input())
	lista_numero.append(numero)
	
maior = lista_numero[0]

for item in range(len(lista_numero)):
	if lista_numero[item] > maior:
		maior = lista_numero[item]

print maior

for item in range(len(lista_numero)):
	if maior == lista_numero[item]:
		posicao = item + 1
		print posicao
