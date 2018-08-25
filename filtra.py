#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: filtra urls

def filtra_urls(l):
	links = []
	for i in range(len(l)):
		if 'google.com' in l[i]:
			links.append(l[i])
	
	return links
