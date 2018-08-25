#coding: utf-8
while True:
	entrada = raw_input()
	dados = entrada.split()
	x = int(dados[0])
	y = int(dados[1])
	if x == 0 or y == 0:
		break
	if x > 0 and y > 0:
		print "primeiro"
	elif x < 0 and y > 0:
		print "segundo"
	elif x < 0 and y < 0:
		print "terceiro"
	elif x > 0 and y < 0:
		print "quarto"
	
