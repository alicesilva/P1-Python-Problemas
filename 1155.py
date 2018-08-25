#coding: utf-8
numerador = 1
denominador = 0
s = 0

for i in range(100):
	denominador += 1
	s += float(numerador) / denominador

print "%.2f" %s
