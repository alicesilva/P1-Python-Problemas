#coding: utf-8
import math
A = float(raw_input())
B = float(raw_input())
C = float(raw_input())
delta = B ** 2 - 4 * A * C
if A == 0 or delta < 0:
	print "Impossivel calcular"
elif delta > 0 and A != 0:
	r1 = (-B + math.sqrt(delta)) / (2 * A)
	r2 = (-B - math.sqrt(delta)) / (2 * A)
	print "R1 = %.5f" %(r1)
	print "R2 = %.5f" %(r2)
