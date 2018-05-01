# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Analytics votação

def conta_votos(votacoes,id_prop):
	contador = []
	cont_sim = 0
	cont_nao = 0
	for i in range(len(votacoes)):
		votos = votacoes[i].split(",")
		if votos[1] == str(id_prop):
			if votos[-1] == 'sim':
				cont_sim += 1
			else:
				cont_nao += 1
	
	contador.append(cont_sim)
	contador.append(cont_nao)
	return contador


