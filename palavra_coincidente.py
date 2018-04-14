#coding: utf-8
palavra1 = raw_input()
palavra2 = raw_input()
contador = 0
print "Letras coincidentes"
for i in range(len(palavra1)):
	for item in range(len(palavra2)):
		if palavra2[item] == palavra1[i] and item == i:
			contador += 1
			print "'%s' na poição %d" %(palavra2[item],item+1),

percentual = float(contador) / (len(palavra1) + len(palavra2)) * 100.0
print "Total de letras coincidentes: %d (%0.f%%)" %(contador,percentual)
