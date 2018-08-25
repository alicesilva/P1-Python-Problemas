#coding: utf-8
valor_hora = float(raw_input("Quanto você ganha por hora? ")) 
numeros_horas = int(raw_input("Número de horas trabalhadas no mês? "))

salario_bruto = valor_hora * numeros_horas

inss = 11.0/100 * salario_bruto
imposto_renda = 8.0/100 * salario_bruto
sindicato = 5.0/100 * salario_bruto

descontos = inss + imposto_renda + sindicato

salario_liquido = salario_bruto - descontos

print salario_bruto
print inss
print sindicato
print salario_liquido

 
