#coding: utf-8

def professores(alocacao, disciplina):
	valor = alocacao.get(disciplina)
	if valor == None:
		return 0
	else:
		return len(valor)
