# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Plif plof
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
soma = numero1 + numero2 + numero3
if soma % 3 == 0 and soma % 5 != 0:
	print "plif"
elif soma % 5 == 0 and soma % 3 != 0:
	print "plof"
elif soma % 3 == 0 and soma % 5 == 0:
	print "plifplof"
else:
	print soma
