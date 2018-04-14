# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Quantidade e média de números pares
lista = []
soma = 0
contador_pares = 0.0
contador_media = 0

n = int(raw_input())

for i in range(n):
	numero = int(raw_input())
	lista.append(numero)
	if numero % 2 == 0:
		contador_pares +=1
		soma += numero

media = soma / contador_pares

for i in range(len(lista)):
	if lista[i] < media:
		contador_media += 1

print "soma: %d" %soma
print "média: %.1f" %media
print "%d número(s) abaixo da média" %(contador_media)

	
