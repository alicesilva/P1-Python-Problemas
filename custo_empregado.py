# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Custo empregado

salario_base = float(raw_input())
dias = int(raw_input())
custo_transporte = float(raw_input())

transporte = dias * custo_transporte

if transporte > 6/100.0 * salario_base:
	vale_empregado = 6/100.0 * salario_base
	vale = transporte - 6/100.0 * salario_base
else:
	vale_empregado = 0
	vale = 0
if salario_base <= 1317.07:
	descontos = 8/100.0 * salario_base
elif salario_base >= 1317.08 and salario_base <= 2195.12:
	descontos = 9/100.0 * salario_base
else:
	descontos = 11/100.0 * salario_base

empregador = salario_base + 8/100.0 * salario_base + 12/100.0 * salario_base + vale

salario_liquido = salario_base - descontos - vale_empregado

print "O salário base é R$ %.2f" %salario_base
print "O custo mensal para o empregador é de R$ %.2f" %empregador
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" %salario_liquido
