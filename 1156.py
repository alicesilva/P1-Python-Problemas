#coding: utf-8
numerador = 1
denominador = 1
s = 0

for i in range(20):
	numerador += 2
	denominador *= 2
	s += float(numerador) / denominador
s = 1 + s
print "%.2f" %s
