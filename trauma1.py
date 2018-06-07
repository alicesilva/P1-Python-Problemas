# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Hospital de trauma

def cadastra(nome,prioridade):
	ordem = []
	for i in range(len(prioridade)):
		if prioridade[i] == "vermelho":
			ordem.append(nome[i])
	for i in range(len(prioridade)):
		if prioridade[i] == "laranja":
			ordem.append(nome[i])
	for i in range(len(prioridade)):
		if prioridade[i] == "amarelo":
			ordem.append(nome[i])
	for i in range(len(prioridade)):
		if prioridade[i] == "verde":
			ordem.append(nome[i])
	for i in range(len(prioridade)):
		if prioridade[i] == "azul":
			ordem.append(nome[i])
	
	return ordem

def resumo(prioridade):
	contadores = []
	cont_vermelho = 0
	cont_laranja = 0
	cont_amarelo = 0
	cont_verde = 0
	cont_azul = 0
	for i in range(len(prioridade)):
		if prioridade[i] == "vermelho":
			cont_vermelho += 1
		if prioridade[i] == "laranja":
			cont_laranja += 1
		if prioridade[i] == "amarelo":
			cont_amarelo += 1
		if prioridade[i] == "verde":
			cont_verde += 1
		if prioridade[i] == "azul":
			cont_azul += 1
	contadores.append(cont_vermelho)
	contadores.append(cont_laranja)
	contadores.append(cont_amarelo)
	contadores.append(cont_verde)
	contadores.append(cont_azul)
	
	return contadores

	
	
nome = []
prioridade = []
while True:
	entrada = raw_input()
	if entrada == "fim":
		break
	dados = entrada.split()
	nome.append(dados[0])
	prioridade.append(dados[1])
	
lista = cadastra(nome,prioridade)
lista1 = resumo(prioridade)

for i in range(len(lista)):
	print lista[i]
	
print "---"


print "vermelho: %d" %lista1[0]
print "laranja: %d" %lista1[1]
print "amarelo: %d" %lista1[2]
print "verde: %d" %lista1[3]
print "azul: %d" %lista1[4]
print "---"
