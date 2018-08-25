#coding: utf-8
n = int(raw_input())
soma = 0
notas = []

for i in range(n-1):
	nota = float(raw_input())
	soma += nota
	notas.append(nota)

print len(notas)

for i in range(len(notas)):
	print notas[i],

print

for i in range(len(notas)):
	print notas[(len(notas)-1-i)]


print soma

media = soma / len(notas)

print media

cont_maiores = 0
cont_abaixo = 0

for i in range(len(notas)):
	if notas[i] > media:
		cont_maiores += 1
	if notas[i] < 7.0:
		cont_abaixo += 1

print cont_maiores
print cont_abaixo

print "Obrigado!"
