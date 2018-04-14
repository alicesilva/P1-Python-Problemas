#coding: utf-8
nova_palavra = ""
palavra = raw_input()
for i in range(len(palavra)):
	if palavra[i] != " ":
		nova_palavra += palavra[i] * 2
	else:
		nova_palavra += " "

print nova_palavra

if len(nova_palavra) >= 13:
	print "senha segura"
else:
	print "senha insegura"

		
