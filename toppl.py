#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: toppl

def filtra_alunos(alunos, inscritos, media):
	cont1 = 0
	for i in range(len(alunos)-1,-1,-1):
		cont = 0
		for j in range(len(inscritos)):
			if alunos[i][0] != inscritos[j]:
				cont += 1
		if cont == len(inscritos):
			alunos.pop(i)
			cont1 += 1
	for i in range(len(alunos)-1,-1,-1):
		if alunos[i][1] < media:
			alunos.pop(i)
			cont1 += 1
	
	return cont1


