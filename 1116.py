#coding: utf-8
n = int(raw_input())
for i in range(n):
	entrada = raw_input()
	dados = entrada.split()
	x = int(dados[0])
	y = int(dados[1])
	if y == 0:
		print "divisao impossivel"
	else:
		divisao = float(x) / y
		print "%.1f" %divisao
