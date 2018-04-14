# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Sistema de metas de venda mensal
lista = []
soma = 0
meta = float(raw_input())
meta_individual = 1/6.0 * meta

for i in range(6):
	vendas = float(raw_input())
	soma += vendas
	if vendas >= meta_individual:
		lista.append(vendas)
		
	
if soma >= meta and len(lista) == 6:
	print "Total de vendas: R$ %.2f (meta atingida)" %(soma)
	print "----"
	print "Bonificação:"
	
	for i in range(len(lista)):
		bonificacao = 0.01 * lista[i]
		print "Funcionário %d: R$ %.2f" %(i + 1, bonificacao)

elif soma< meta or len(lista) != 6:
	print "Total de vendas: R$ %.2f (meta não foi atingida)" %(soma)
	print "----"
