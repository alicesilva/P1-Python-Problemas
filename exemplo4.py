#coding: utf-8
A = float(raw_input())
B = float(raw_input())
C = float(raw_input())
if A >= B + C:
	print "NAO FORMA TRIANGULO"
if A**2 == B**2 + C**2:
	print "TRIANGULO RETANGULO"
if A**2 > B**2 + C**2:
	print  "TRIANGULO OBTUSANGULO"
if A**2 < B**2 + C**2:
	print "TRIANGULO ACUTANGULO"
if A==B==C:
	print "TRIANGULO EQUILATERO"
if A==B or B==C or A==C:
	print "TRIANGULO ISOSCELES"
