# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Divisores próprios pares
n = int(raw_input())
for i in range(2, n, 2):
	if n % i == 0:
		print i
	
