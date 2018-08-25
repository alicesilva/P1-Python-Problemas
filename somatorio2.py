#coding: utf-8
def somatorio2(n):
	soma1 = 0
	soma2 = 0
	for i in range(1,n+1):
		soma1 += i
		soma2 += 3 * i ** 3
	
	fatorial = 1
	n1 = soma1 * 2
	for i in range(1,n1+1):
		fatorial *= i
	
	print fatorial + soma2

n = 2
somatorio2(n)
