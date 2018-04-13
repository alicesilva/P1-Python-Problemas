# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Espaço por vírgula

frase = raw_input()
i = int(raw_input())
j = int(raw_input())

for k in range(i,j):
	if frase[k] != " ":
		print frase[k],
	else:
		print ",",
