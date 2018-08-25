#coding: utf-8
import math
area = float(raw_input())
if area <= 54:
	print "1 lata"
	print "R$ 18.00"
else:
	latas = area / 54.0
	total = latas * 18
	print "%.1f latas" %latas
	print "R$ %.2f" %total
