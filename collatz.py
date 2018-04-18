# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# A conjectura de collatz

n = int(raw_input())

print n

while n > 1:
	if n % 2 == 0:
		n = n / 2
		print n
	else:
		n = n * 3 + 1
		print n
	
