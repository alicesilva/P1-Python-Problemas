# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Meu posto

pontos = 0.0
nomes = []
cpfs = []
postos = []

while True:
	operacao = raw_input()
	if operacao == "cadastrar":
		cpf = raw_input()
		nome = raw_input()
		posto = raw_input()
		if cpf in cpfs:
			print "Usuário já existente."
		else:
			print "Usuário cadastrado com sucesso."
		nomes.append(nome)
		cpfs.append(cpf)
		postos.append(posto)
		pontos += 300
	if operacao == "atualizar":
		cpf = raw_input()
		posto = raw_input()
		if cpf not in cpfs:
			print "Usuário inexistente."
		else:
			print "Usuário atualizado com sucesso."
		if posto in postos:
			pontos += 200
		else:
			pontos += 100
		cpfs.append(cpf)
		postos.append(posto)
	if operacao == "consultar":
		cpf = raw_input()
		if cpf in cpfs:
			print "Nome: %s" %nome
			print "CPF: %s" %cpf
			print "Saldo: %.2f" %pontos
		else:
			print "Usuário inexistente."
		cpfs.append(cpf)
	if operacao == "finalizar":
		break
	
