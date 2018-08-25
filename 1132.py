#coding: utf-8
x = int(raw_input())
y = int(raw_input())
maior = x
if y > maior:
	maior = y
	menor = x
else:
	maior = x
	menor = y
soma = 0
for i in range(menor, maior+1):
	if i % 13 != 0:
		soma += i
print soma
