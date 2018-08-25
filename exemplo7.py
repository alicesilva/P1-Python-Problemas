#coding: utf-7
carac1 = raw_input()
carac2 = raw_input()
carac3 = raw_input()
if carac1 == "vertebrado":
	if carac2 == "ave":
		if carac3 == "carnivoro":
			print "aguia"
		elif carac3 == "onivoro":
			print "pomba"
	if carac2 == "mamifero":
		if carac3 == "onivoro":
			print "homem"
		elif carac3 == "herbivoro":
			print "vaca"
if carac1 == "invertebrado":
	if carac2 == "inseto":
		if carac3 == "hematofago":
			print "pulga"
		elif carac3 == "herbivoro":
			print "lagarta"
	if carac2 == "anelideo":
		if carac3 == "hematofago":
			print "sanguessuga"
		elif carac3 == "onivoro":
			print "minhoca"
		
