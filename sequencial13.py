#coding: utf-8
altura = float(raw_input())
sexo = raw_input()
if sexo == "masculino" or "Masculino" or "MASCULINO":
	pesoideal = (72.7*altura) - 58
else:
	pesoideal = (62.1*altura) - 44.7

peso = float(raw_input())
if peso == pesoideal:
	print "dentro do peso."
elif peso < pesoideal:
	print "abaixo do peso."
else:
	print "acima do peso."
