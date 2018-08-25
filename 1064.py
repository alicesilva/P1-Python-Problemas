#coding: utf-8
soma = 0
contador = 0
for i in range(6):
	numero = float(raw_input())
	if numero > 0:
		contador += 1
		soma +=numero

media = float(soma) / contador

print "%d valores positivos" %(contador)
print "%.1f" %(media)
