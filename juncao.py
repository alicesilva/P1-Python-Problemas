# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Junção de turmas

def junta_listas(lista1, lista2):
	nova_lista = []
	for i in range(len(lista1)):
		nova_lista.append(lista1[i])
	for i in range(len(lista2)):
		nova_lista.append(lista2[i])
		
	for i in range(len(nova_lista)):
		for j in range(len(nova_lista)):
			if nova_lista[i] <= nova_lista[j]:
				nova_lista[i],nova_lista[j] = nova_lista[j],nova_lista[i]

	
	return nova_lista


turma1 = raw_input()
turma2 = raw_input()
turma3 = raw_input()

listas1 = turma1.split()
listas2 = turma2.split()
listas3 = turma3.split()

lista1 = []
lista2 = []
lista3 = []

for i in range(len(listas1)):
	if listas1[i] != "Turma1:":
		lista1.append(listas1[i])
for i in range(len(listas2)):
	if listas2[i] != "Turma2:":
		lista2.append(listas2[i])
for i in range(len(listas3)):
	if listas3[i] != "Turma3:":
		lista3.append(listas3[i])
	
lista4 = junta_listas(lista1,lista2)
lista5 = junta_listas(lista4,lista3)

for i in range(len(lista5)):
	print "%d. %s" %(i+1,lista5[i])


