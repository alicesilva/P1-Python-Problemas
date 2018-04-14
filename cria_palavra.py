# coding: utf-8
# Aluna:Alice Fernandes Silva/UFCG, 2015.1, Programação 1
# Criação de uma nova palavra

palavra = raw_input()
numero_apoio = raw_input()

nova_palavra = ""

for i in range(len(palavra)):
	nova_palavra += palavra[i]
	nova_palavra += (palavra[i] * int(numero_apoio[-(i+1)]))

print nova_palavra
	
