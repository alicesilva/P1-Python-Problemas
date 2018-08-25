#coding: utf-8
notas = []
soma = 0
while True:
	nota = float(raw_input())
	notas.append(nota)
	cont = 0
	for i in range(len(notas)):
		if notas[i] > 0.0 and notas[i] < 10.0:
			cont += 1
	if cont == 2:
		break

