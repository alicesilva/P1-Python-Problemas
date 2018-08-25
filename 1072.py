#coding: utf-8
n = int(raw_input())
contador = 0
contador1 = 0
for i in range(n):
	x = int(raw_input())
	if x >= 10 and x <= 20:
		contador += 1
	else:
		contador1 += 1

print "%d in" %(contador)
print "%d out" %(contador1)
