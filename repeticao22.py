#coding: utf-8
numero = int(raw_input())

cont_divisivel = 0

for i in range(1,numero+1):
	if numero % i == 0:
		cont_divisivel += 1

if cont_divisivel == 2:
	print "É primo."
else:
	print "Não é primo."
	for i in range(1, numero+1):
		if numero % i == 0:
			print i
