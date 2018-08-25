#coding: utf-8
A = float(raw_input())
B = float(raw_input())
C = float(raw_input())
area_triangulo = (A * C) / 2.0
area_circulo = 3.14159 * C ** 2
area_trapezio = (C *(A+B)) / 2.0
area_quadrado = B ** 2
area_retangulo = A * B
print "TRIANGULO: %.3f" %area_triangulo
print "CIRCULO: %.3f" %area_circulo
print "TRAPEZIO: %.3f" %area_trapezio
print "QUADRADO: %.3f" %area_quadrado
print "RETANGULO: %.3f" %area_retangulo
