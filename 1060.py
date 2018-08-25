#coding: utf-8
contador = 0
for i in range(6):
	numero = float(raw_input())
	if numero > 0:
		contador += 1

print "%d valores positivos" %(contador)
