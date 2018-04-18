# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Resumo compras

preco = raw_input()

soma = 0
contador = 0
maior = 0
media = 0

while preco != "fim":
	soma += float(preco)
	contador += 1
	preco = raw_input()
	media = soma / contador
	if preco != "fim":
		if float(preco) > maior:
			maior = float(preco)

print "O valor médio por produto foi R$ %.2f. O produto mais caro custa \
R$ %.2f." %(media,maior)

	
