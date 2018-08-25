#coding: utf-8
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

maiorab = (a+b+abs(a-b)) / 2

if c > maiorab:
	maior = c
else:
	maior = maiorab

print "%d eh o maior" %maior
