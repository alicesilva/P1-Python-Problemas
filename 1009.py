#coding: utf-8
nome = raw_input()
salario = float(raw_input())
venda = float(raw_input())
comissao = 15/100.0 * venda
total = salario + comissao
print "TOTAL = R$ %.2f" %total
