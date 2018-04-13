#coding: utf-8
def conta_votos(votacoes,id_prop):
	cont_sim = 0
	cont_nao = 0
	resultados = []
	for i in range(len(votacoes)):
		dados = votacoes[i].split(",")
		if dados[1] == str(id_prop) and dados[4] == "sim":
			cont_sim += 1
		elif dados[1] == str(id_prop) and dados[4] == "nao":
			cont_nao += 1
	
	resultados.append(cont_sim)
	resultados.append(cont_nao)
	
	return resultados
	
			
		
