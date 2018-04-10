# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Produto em uma pg
a1 = int(raw_input())
a2 = int(raw_input())
numero = int(raw_input())
razao = a2/a1
n = (numero*(numero - 1) / 2)
pn = a1 ** numero * razao ** n
print pn
