#coding: utf-8
while True:
	entrada = raw_input()
	dados = entrada.split()
	x = int(dados[0])
	y = int(dados[1])
	if x == y:
		break
	if x > y:
		print "Decrescente"
	else:
		print "Crescente"
