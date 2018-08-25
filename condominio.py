#coding: utf-8
#Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
#exercicio: construção de condominio
lado1 = float(raw_input())
lado2 = float(raw_input())
area_casa = float(raw_input())
area_terreno = lado1*lado2
quantidade_casas = area_casa/ int(area_terreno) * 100
print "%.0f casa(s) pode(m) ser construída(s) no terreno." %(quantidade_casas)
