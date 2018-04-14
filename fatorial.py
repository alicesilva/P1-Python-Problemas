# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Fatorial

n = int(raw_input())
fatorial = 1
for i in range(n,0,-1):
	fatorial *= i

print fatorial
