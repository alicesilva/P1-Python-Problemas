#coding: utf-8
numeros = []
while True:
	entrada = raw_input()
	dados = entrada.split()
	m = int(dados[0])
	n = int(dados[1])
	if m <= 0 or n <=0:
		break
	maior = m
	if n > maior:
		maior = n
		menor = m
	else:
		maior = m
		menor = n
	soma = 0
	for i in range(menor,maior+1):
		soma += i
		print i,
	print "Sum=%d" %soma
	
