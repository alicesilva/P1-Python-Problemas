#coding: utf-8
idades = []
alturas = []
soma = 0
i = 0

for i in range(30):
	i += 1
	print "Aluno %d:" %i
	idade = int(raw_input())
	altura = float(raw_input())
	idades.append(idade)
	alturas.append(altura)
	soma += altura

media = soma / 30

cont = 0

for i in range(len(idades)):
	for i in range(len(altura)):
		if idades[i] > 13 and altura[i] < media:
			cont += 1

print cont		


	
