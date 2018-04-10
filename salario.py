# coding: utf-8
# Calculo e impressão da folha de pagamento de um empregado

salario_atual = float(raw_input("Salário atual? "))
aumento = float(raw_input("Aumento projetado (em %)? "))
inss = float(raw_input("Nova contribuição previdenciária (em %)? "))
novo_salario = salario_atual * (1+aumento/100)
contribuicao = (novo_salario * (inss/100.0))
salario_liquido = novo_salario - contribuicao

print
print "Dados do novo salário\n==="
print "Salário: R$ %.2f" %(novo_salario)
print "Contribuição previdenciária: R$ %.2f (%.1f%%)" %(contribuicao,inss)
print "Salário líquido: R$ %.2f" %(salario_liquido)
