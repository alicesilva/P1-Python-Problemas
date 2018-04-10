# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Ano bissexto
ano = int(raw_input())
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
	print "%d é bissexto" %(ano)
else:
	print "%d não é bissexto" %(ano)
