#coding: utf-8
soma = 0
cont = 0
while True:
	idade = int(raw_input())
	if idade < 0:
		break
	soma += idade
	cont += 1

media = float(soma) / cont

print "%.2f" %media
