# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Análise de variação do salário minimo

contador_abaixo = 0.0
contador_acima = 0.0
abaixo = 0.0
acima = 0.0
lista = []

inicio = int(raw_input())
final = int(raw_input())

for i in range(inicio, final + 1, 1):
	salario = float(raw_input())
	lista.append(salario)
	
for item in range(len(lista)):
	if lista[item] <= 100:
		contador_abaixo += 1
		abaixo += lista[item]
		percentual1 = (contador_abaixo / len(lista)) * 100
		media1 = abaixo / contador_abaixo
	else:
		contador_acima += 1
		acima += lista[item]
		percentual2 = (contador_acima / len(lista)) * 100
		media2 = acima / contador_acima

if contador_abaixo == 0:
	percentual1 = 0

print "%d ano(s) abaixo (%.0f%% dos anos)" %(contador_abaixo,percentual1)

if contador_abaixo != 0:
		print "média dos anos abaixo: U$ %.2f" %(media1)

print "%d ano(s) acima (%.0f%% dos anos)" %(contador_acima ,percentual2)
print "média dos anos acima: U$ %.2f" %(media2)
		
		
