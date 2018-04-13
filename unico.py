#coding: utf-8
def unico(string):
	nova_string = ""
	for i in range(len(string)-1):
		if string[i] != string[i+1]:
			nova_string += string[i]
	
	if len(string) != 0:
		nova_string += string[-1]
	
	if len(string) == 2 and string[0] == string[1]:
		nova_string = string[0]
	
	if len(string) == 1:
		nova_string = string
		
	print nova_string
	return nova_string
