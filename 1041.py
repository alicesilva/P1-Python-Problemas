#coding: utf-8
entrada = raw_input()
entrada1 = entrada.split()
x = float(entrada1[0])
y = float(entrada1[1])

if x == 0 or y == 0:
	if x==y==0:
		print "Origem"
	elif x == 0:
		print "Eixo Y"
	elif y == 0:
		print "Eixo X"
	
if x != 0 and y != 0: 
	if x > 0 and y > 0:
		print "Q1"
	elif x < 0 and y > 0:
		print "Q2"
	elif x < 0 and y < 0:
		print "Q3"
	elif x > 0 and y < 0:
		print "Q4"
