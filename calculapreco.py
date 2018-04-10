# coding: utf-8
# Calculo do preço de venda de um produto

import math

cust_entrada = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
imposto = float(raw_input())
comissao = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())
prec_venda = (cust_entrada + despesas + lucro)*100/ (100 - imposto - comissao - descontos - encargos)
prec_venda1 = math.ceil(prec_venda) + 0.61
arre = math.ceil(prec_venda)

print "Preço de venda é R$ %.2f (R$ %.2f + R$ 0.61)" % (prec_venda1,arre)
