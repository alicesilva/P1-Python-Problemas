#coding: utf-8
respostas = []
telefone = raw_input("Telefonou para a vítima? ") 
local_crime = raw_input("Esteve no local do crime? ")
local = raw_input("Mora perto da vítima? ")
divida = raw_input("Devia para a vítima? ")
trabalho = raw_input("Já trabalhou com a vítima? ")

respostas.append(telefone)
respostas.append(local_crime)
respostas.append(local)
respostas.append(divida)
respostas.append(trabalho)

cont_sim = 0
cont_nao = 0
for i in range(len(respostas)):
	if respostas[i] == "sim" or respostas[i] == "Sim" or respostas == "SIM":
		cont_sim += 1
	else:
		cont_nao += 1

if cont_sim == 2:
	print "Suspeita"
elif cont_sim == 3 or cont_sim == 4:
	print "Cúmplice"
elif cont_sim == 5:
	print "Assassino"
else:
	print "Inocente"
