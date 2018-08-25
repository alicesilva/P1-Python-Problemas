#coding: utf-8
habitantesA = float(raw_input())
porcetagemA = float(raw_input())
habitantesB = float(raw_input())
porcentagemB = float(raw_input())

crescimentoA = porcetagemA / 100.0 * habitantesA
crescimentoB = porcentagemB / 100.0 * habitantesB

somaA = habitantesA + crescimentoA
somaB = habitantesB + crescimentoB
divisao = somaB / somaA

print "%.1f anos." %divisao
