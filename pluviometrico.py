#coding: utf-8

def maior_indice_plu(tabela,cidade):
	nova_s = ""
	maior = tabela[0][0]
	linha = 0
	for i in range(len(tabela)):
		for j in range(len(tabela[i])):
			if tabela[i][j] > maior:
				maior = tabela[i][j]
				linha = i
	
	nova_s += cidades[linha] + " " + str(maior)
	
	return nova_s
