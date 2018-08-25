#coding: utf-8
x = int(raw_input())
y = int(raw_input())
soma = 0
if x < y:
	menor = x
	maior = y
else:
	menor = y
	maior = x

for i in range(menor+1,maior):
	if i % 2 != 0:
		soma += i

print soma
