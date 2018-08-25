#coding: utf-8
lado1 = float(raw_input())
lado2 = float(raw_input())
lado3 = float(raw_input())

if (lado1+lado2) > lado3 or (lado2+lado3) > lado1 or (lado1+lado3) > lado2:
	print "É um triângulo"
	if lado1 == lado2 == lado3:
		print "Triângulo Equilátero"
	elif lado1==lado2!=lado3  or lado3==lado2!=lado1 or lado1==lado3!=lado2:
		print "Triângulo Isósceles"
	else:
		print "Triângulo Escaleno"

