# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1

login1 = raw_input()
espaco1 = float(raw_input())
login2 = raw_input()
espaco2 = float(raw_input())
login3 = raw_input()
espaco3 = float(raw_input())
tamanho_1 = espaco1/(1024**2)
tamanho_2 = espaco2/(1024**2)
tamanho_3 = espaco3/(1024**2)
espaco_total = tamanho_1 + tamanho_2 + tamanho_3
espaco_medio = espaco_total/3.0

print "SPLab - Espaço utilizado pelos usuários\n---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado"
print
print "1, %s, %.2f MB" %(login1,tamanho_1)
print "2, %s, %.2f MB" %(login2,tamanho_2)
print "3, %s, %.2f MB" %(login3,tamanho_3)
print
print "Espaço total ocupado: %.2f MB" %(espaco_total)
print "Espaço médio ocupado: %.2f MB" %(espaco_medio)
