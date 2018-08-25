#coding: utf-8
def somatorio(n):
	soma = 0
	for i in range(1, n+1):
		soma += 2*i**2 + 3*i**3 + 4*i**4
	print soma
