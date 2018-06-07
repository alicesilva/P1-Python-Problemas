# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Calcula áreas com funções

import math

def areaQuadrado(lado):
	area = lado ** 2
	return area

def areaTriangulo(base,altura):
	area = (base * altura) / 2.0
	return area

def areaCirculo(raio):
	area = math.pi * (raio ** 2)
	return area

while True:
	figura = raw_input()
	if figura == "fim":
		break
	dados = figura.split()
	if dados[0] == "Q":
		lado = float(dados[1])
		print "A área do quadrado é %.2f" %areaQuadrado(lado)
	if dados[0] == "C":
		raio = float(dados[1])
		print "A área do círculo é %.2f" %areaCirculo(raio)
	if dados[0] == "T":
		base = float(dados[1])
		altura = float(dados[2])
		print "A área do triangulo é %.2f" %areaTriangulo(base,altura)
	
		
