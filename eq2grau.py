# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Corrigindo equações
import math
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
delta = b ** 2 - 4 * a * c
if delta > 0:
	x1 = ((-b) + math.sqrt(delta)) / (2.0 * a)
	x2 = ((-b) - math.sqrt(delta)) / (2.0 * a)
	print "x1 = %.2f" %(x1)
	print "x2 = %.2f" %(x2)
elif delta == 0:
	x = -b/(2.0*a)
	print "x = %.2f" %(x)
else:
	print "sem raizes reais"

