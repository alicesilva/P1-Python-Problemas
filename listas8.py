#coding: utf-8
i = 0
idades = []
alturas = []

for i in range(5):
	i += 1
	print "Pessoa %d:" %i
	idade = int(raw_input())
	altura = float(raw_input())
	idades.append(idade)
	alturas.append(altura)

for i in range(len(idades)):
	print idades[(len(idades)-1-i)]

for i in range(len(alturas)):
	print alturas[(len(alturas)-1-i)]
	
