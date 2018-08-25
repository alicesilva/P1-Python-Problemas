#coding: utf-8
numero = int(raw_input())

print "Tabuada de %d:" %numero

for i in range(1, 11):
	multiplicacao = numero * i
	print "%d X %d = %d" %(numero,i,multiplicacao)
