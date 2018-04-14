# coding: utf-8
# Aluna:Alice Fernandes Silva/UFCG, 2015.1, Programação 1
# Produzindo um Senha Segura

palavra = raw_input()

senha = ""

for i in palavra:
	if i != " ":
		senha += i * 2
	else:
		senha += " "

print senha

if len(senha) >= 13:
	print "senha segura"
else:
	print "senha insegura"
	
