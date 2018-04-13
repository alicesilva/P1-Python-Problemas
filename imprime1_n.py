#coding: utf-8
def imprime1(n):
	indices = []
	for i in range(n):
		i += 1
		for j in range(1,i+1):
			print j,
		print

n = int(raw_input())
imprime1(n)
			
