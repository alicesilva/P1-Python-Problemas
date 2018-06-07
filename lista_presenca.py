# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Lista presença

def cria_lista_presenca(turmas, nomes, turma):
	nova_lista = []
	for i in range(len(turmas)):
		if turmas[i] == turma:
			nova_lista.append(nomes[i])
	
	return nova_lista
