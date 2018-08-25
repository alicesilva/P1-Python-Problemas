#coding: utf-8
contador = 0
for i in range(5):
	numero = int(raw_input())
	if numero % 2 == 0:
		contador += 1

print "%d valores pares" %contador
