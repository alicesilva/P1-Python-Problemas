# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Validação de triângulos
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
if abs((a-b)) < a < b+c and abs((a-c)) < b < a+c and abs((a-b)) < c < a+b:
	perimetro = a + b + c
	print "triangulo valido. %d" %(perimetro)
else:
	print "triangulo invalido."
