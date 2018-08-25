#coding: utf-8
nome = raw_input()
senha = raw_input()

while nome == senha:
	print "Erro"
	nome = raw_input()
	senha = raw_input()
