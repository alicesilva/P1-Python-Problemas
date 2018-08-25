#coding: utf-8

n = int(raw_input())

for i in range(n):
	numero = int(raw_input())
	cont = 0
	for i in range(1,numero):
		if numero % i == 0:
			cont += 1
	if cont == 1:
		print "%d eh primo" %numero
	else:
		print "%d nao eh primo" %numero
	
