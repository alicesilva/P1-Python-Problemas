#coding: utf-8
def somatorio3(n):
	soma1 = 0
	for i in range(1,2*n+1):
		soma1 += 2 * i ** 2
	
	soma2 = 0
	for i in range(1,n+1):
		soma2 += i
	
	n1 = soma2 * 3
	fatorial = 1
	for i in range(1,n1+1):
		fatorial *= i
	
	print soma1 - fatorial 

		
