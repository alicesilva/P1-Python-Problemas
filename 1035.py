#coding: utf-8
A = int(raw_input())
B = int(raw_input())
C = int(raw_input())
D = int(raw_input())
if B>C and D>A and (C+D)>(A+B) and C>0 and D>0 and A%2 == 0:
	print "Valores aceitos"
else:
	print "Valores nao aceitos"
