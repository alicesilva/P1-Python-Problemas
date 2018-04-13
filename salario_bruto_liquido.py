#coding: utf-8
#Alice Fernandes Silva/UFCG, 2015.1, Programação 1

nome = raw_input()
quant_hoex = float(raw_input())
salario_minimo = float(raw_input())
valor_hoex = float(raw_input())
salario_hoex = quant_hoex * valor_hoex
salario_bruto = 4 * salario_minimo + salario_hoex
desconto_inss = (12/100.0) * salario_bruto
desconto_imposto = (20/100.0) * salario_bruto
descontos = desconto_inss + desconto_imposto
salario_liquido = salario_bruto - descontos

print "O Salário Bruto de %s é de R$ %.2f" % (nome,salario_bruto)
print "O Salário Líquido de %s é de R$ %.2f" % (nome,salario_liquido)
