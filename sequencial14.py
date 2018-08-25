#coding: utf-8
peso = float(raw_input())
excesso = peso - 50
multa = excesso * 4
if excesso <= 0 and multa <= 0:
	print "ZERO"
else:
	print excesso
	print multa
