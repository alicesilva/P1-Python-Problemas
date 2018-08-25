#coding: utf-8
inicio_jogo = int(raw_input())
fim_jogo = int(raw_input())
if inicio_jogo >= fim_jogo:
	duracao = 24 - (inicio_jogo - fim_jogo)
	print "O JOGO DUROU %d HORA(S)" %(duracao)
else:
	duracao1 = fim_jogo - inicio_jogo
	print "O JOGO DUROU %d HORA(S)" %(duracao1)
