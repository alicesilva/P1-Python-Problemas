# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Cria login

def cria_login(nome):
	dados = nome.split()
	login = dados[0].lower()
	for i in range(1,len(dados)):
		if dados[i] != "do" and dados[i] != "da" and dados[i] != "de":
			login += dados[i][0].lower()
	
	return login


while True:
	nome = raw_input()
	if nome == "fim":
		break
	print "%s: %s" %(nome,cria_login(nome))

		
