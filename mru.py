# coding: utf8
# Calculo do movimento retilíneo uniforme de um veículo

pos_ini= float(raw_input("posição inicial (m)? "))
veloc = float(raw_input("velocidade (m/s)? "))
temp = float(raw_input("tempo (s)? "))
s_final = pos_ini + veloc*temp
print "Posição final do móvel \nS(%.1f) = %.1f m" %(temp,s_final)
