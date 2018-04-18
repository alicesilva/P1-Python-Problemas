# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Múltiplos de 5

lim = int(raw_input())

for i in range(5,lim,5):
	if i % 2 == 0:
		print i
