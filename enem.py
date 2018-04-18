# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Aprovados no enem

nome = []
nota = []
cont = 0

entrada = raw_input()


while entrada != "fim":
	dados = entrada.split()
	nome.append(dados[0])
	nota.append(int(dados[1]))
	entrada = raw_input()
		
nota_corte = int(raw_input())

for i in range(len(nome)):
	for item in range(len(nota)):
		if int(nota[item]) >= nota_corte:
			cont += 1
			print "%s, %d" %(nome[item],nota[item])
	break

if cont == 0:
	print "Nenhum candidato aprovado."
		
