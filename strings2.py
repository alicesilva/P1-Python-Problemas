#coding: utf-8
nome = raw_input()

for i in range(len(nome)):
	print nome[(len(nome)-1-i)].upper()
