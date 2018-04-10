# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Área de figuras planas
import math
figura = raw_input()
if figura == "círculo":
	raio = float(raw_input())
	area_circulo = math.pi * raio ** 2
	print "Área do círculo: %.2f (cm2)" %(area_circulo)
elif figura == "quadrado":
	lado = float(raw_input())
	area_quadrado = lado ** 2
	print "Área do quadrado: %.2f (cm2)" %(area_quadrado)
elif figura == "triângulo":
	base = float(raw_input())
	altura = float(raw_input())
	area_triangulo = (base * altura) / 2.0
	print "Área do triângulo: %.2f (cm2)" %(area_triangulo)
elif figura == "retângulo":
	base = float(raw_input())
	altura = float(raw_input())
	area_retangulo = base * altura
	print "Área do retângulo: %.2f (cm2)" %(area_retangulo)
