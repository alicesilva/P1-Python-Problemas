#coding: utf-8
n = int(raw_input())

numeros = []

for i in range(n):
	num = int(raw_input())
	numeros.append(num)

for j in numeros:
	if j != 0:
		if j > 0 and j % 2 == 0:
			print "EVEN POSITIVE"
		elif j < 0 and j % 2 == 0:
			print "EVEN NEGATIVE"
		elif j > 0 and j % 2 != 0:
			print "ODD POSITIVE"
		elif j < 0 and j % 2 != 0:
			print "ODD NEGATIVE"
	else:
		print "NULL"
