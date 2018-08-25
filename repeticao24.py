#coding: utf-8
n = int(raw_input())

soma = 0

for i in range(n):
	notas = float(raw_input())
	soma += notas

media = soma / n
	
print media
