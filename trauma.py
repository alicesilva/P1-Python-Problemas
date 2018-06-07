# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Hospital de trauma

def cadastra(nome, prioridade):
	lista = []
	if prioridade == "vermelho":
		lista.append(nome)
	if prioridade == "laranja":
		lista.append(nome)
	if lista == "amarelo":
		amarelo.append(nome)
	if lista == "verde":
		verde.append(nome)
	if lista == "azul":
		azul.append(nome)
	
	return lista
def resumo(lista):
	return len(lista)

while True:
	entrada = raw_input()
	if entrada == "fim":
		break
	dados = entrada.split()
	lista = cadastra(dados[0],dados[1])

for i in range(len(lista)):
	print lista[i]
	
	
