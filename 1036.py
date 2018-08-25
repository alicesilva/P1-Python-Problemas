#coding: utf-8
import math
entrada = raw_input()
entrada1 = entrada.split()
A = float(entrada1[0])
B = float(entrada1[1])
C = float(entrada1[2])
delta = B ** 2 - 4 * A * C
if A == 0 or delta < 0:
	print "Impossivel calcular"
else:
	r1 = (-B + math.sqrt(delta)) / (2 * A)
	r2 = (-B - math.sqrt(delta)) / (2 * A)
	print "R1 = %.5f" %(r1)
	print "R2 = %.5f" %(r2)
