# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Resultado 

def reclassifica(resultado_preliminar, recursos):
	for tuplas in recursos:
		resultado_preliminar.append(tuplas)
	
	for i in range(len(resultado_preliminar)-1):
		for j in range(len(resultado_preliminar)-1):
			if resultado_preliminar[j][1] < resultado_preliminar[j+1][1]:
				resultado_preliminar[j], resultado_preliminar[j+1] = resultado_preliminar[j+1], resultado_preliminar[j]
			if resultado_preliminar[j][1] == resultado_preliminar[j+1][0] and\
				resultado_preliminar[j][2] < resultado_preliminar[j+1][2]:
					resultado_preliminar[j], resultado_preliminar[j+1] = resultado_prelimnar[j+1] = resultado_preliminar[j]
					
		



		
		
