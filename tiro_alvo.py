# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Tiro ao alvo 2

import math

distancia = []
cont = 0

while True:
	x = float(raw_input())
	y = float(raw_input())
	dist = math.sqrt((x)**2 + (y)**2)
	if dist > 200:
		break
	distancia.append(dist)
	menor = distancia[0]
	if dist <= menor:
		print "%.2f cm (melhor tiro)" %dist
	else:
		print "%.2f cm" %dist

soma = 0
menor = distancia[0]

for i in range(len(distancia)):
	soma += distancia[i]
	if distancia[i] < menor:
		menor = distancia[i]
		
media = float(soma)/len(distancia)

print "--"
print "num tiros: %d" %len(distancia)
print "melhor tiro: %.2f cm" %menor
print "distancia media: %.2f cm" %media
	
	
	
