#coding: utf-8
cds = int(raw_input())

soma = 0

for i in range(cds):
	valor = float(raw_input())
	soma += valor

total = soma * cds

print total

for i in range(cds):
	valor_medio = total / valor
	print valor_medio
