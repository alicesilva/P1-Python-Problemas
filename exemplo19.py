#coding: utf-8
A = float(raw_input())
B = float(raw_input())
C = float(raw_input())
if abs(B-C) < A < (B + C)  and  (A-C) < B < (A+C) and (A-B) < C < A + B:
	perimetro = A + B + C
	print "Perimetro = %.1f" %(perimetro)
else: 
	area = (C*(A+B)) /2.0
	print "Area = %.1f" %(area)
	
