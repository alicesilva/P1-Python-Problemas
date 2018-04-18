# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Tiro ao alvo

import math

cont = 0
soma = 0
lista = []

while True:
	entrada = raw_input()
	dados = entrada.split(",")
	x = float(dados[0])
	y = float(dados[1])
	dist = math.sqrt((x**2) + (y**2))
	lista.append(dist)
	if dist > 200:
		break
	print "%.2f" %dist
	soma += dist
	cont += 1
	
if lista[0] > 200:
	cont = 0
	media = 0
else:
	media = soma / float(cont)

print "--"
print "num disparos: %d" %cont
print "distancia media: %.2f" %media

