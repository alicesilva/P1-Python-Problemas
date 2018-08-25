#coding: utf-8
x = int(raw_input())
y = int(raw_input())

menor = x
maior = y

if y < x:
	menor = y
	maior = x
for i in range(menor, maior +1):
	print i
