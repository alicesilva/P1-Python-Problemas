#coding: utf-8
while True:
	X = int(raw_input())
	if X == 0:
		break
	if X % 2 == 0:
		soma = 0
		for i in range(5):
			soma += X
			X += 2
	else:
		X = X + 1
		soma = 0
		for i in range(5):
			soma += X
			X += 2
	print soma
