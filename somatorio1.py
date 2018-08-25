#coding: utf-8
def somatorio1(n):
	fatorial = 1
	n1 = n * 2
	for i in range(1,n1+1):
		fatorial *= i
	soma = fatorial
	for i in range(1,n+1):
		soma += 3 * i ** 3 + 4 * i ** 4
	
	print soma

