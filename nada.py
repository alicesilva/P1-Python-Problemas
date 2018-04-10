# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Depois do 13 nada
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
if numero1 + numero2 == 13 or numero2  + numero3 == 13 or numero1 + numero3 == 13 or numero1+numero2+numero3 == 13:
	print 0
elif numero1 == 13:
	print 0
elif numero2 == 13:
	print numero1
elif numero3 == 13:
	print numero1+numero2
else:
	print numero1 + numero2 + numero3
