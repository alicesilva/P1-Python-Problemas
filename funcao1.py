#coding: utf-8
def imprime(n):
	for i in range(1,n+1):
		print str(i) * i,

n = int(raw_input())
imprime(n)
