# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Porta eletrônica

categorias = []
cont = 0 

while True:
	codigo = raw_input()
	if codigo == "S":
		break
	if codigo[0] == "R":
		categorias.append(codigo)
	if codigo[0] == "P":
		for i in categorias:
			if i[2] == codigo[2]:
				cont += 1
		print cont
		cont = 0

		
