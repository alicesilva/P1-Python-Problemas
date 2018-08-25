#coding: utf-8
notas = []
soma = 0

for i in range(4):
	nota = float(raw_input())
	notas.append(nota)
	soma += nota

for i in range(len(notas)):
	print notas[i]

media = soma / len(notas)

print media
