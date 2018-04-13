# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Números iguais
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
if numero1 == numero2 == numero3:
	print 3
elif numero1==numero2 or numero1==numero3:
	print 2
elif numero2==numero1 or numero2==numero3:
	print 2
elif numero3==numero1 or numero3==numero2:
	print 2
else:
	print 0
