#coding: utf-8
numero = raw_input()

for i in range(len(numero)):
	if numero[i] == ".":
		print "É decimal."
		break
else:
	print "É inteiro"
