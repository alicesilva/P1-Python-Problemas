# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Clássico dos maiorais
gols_campinense = int(raw_input())
gols_treze = int(raw_input())
if gols_campinense > gols_treze:
	print "Campinense"
elif gols_treze > gols_campinense:
	print "Treze"
else:
	print "Empate"
