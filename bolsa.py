# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Economizando a bolsa de estudos

meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
saldos = []
saldo = 0

for i in range(12):
	gastos = int(raw_input())
	saldo += 500 - gastos
	saldos.append(saldo)

maior = saldos[0]

for i in range(len(saldos)):
	if saldos[i] > maior:
		maior = saldos[i]

for item in range(len(saldos)):
	if maior == saldos[item]:
		mes = meses[item]

print mes
	
	
