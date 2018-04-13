# coding: utf-8
# Alice Fernandes Silva/UFCG, 2015.1, Programação 1
# Área do quadrado na circunferência
import math
raio = float(raw_input())
lado_quadrado = raio * math.sqrt(2)
area_quadrado = lado_quadrado**2
area_circ = (math.pi) * raio ** 2
area_cinza = area_circ - area_quadrado
print "Área não comum: %.5f" % (area_cinza)
