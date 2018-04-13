#coding: utf-8
def embaralha(string):
	nova_string = ""
	j = 0
	for i in range(len(string)):
		nova_string += string[len(string) - 1 - j]
		j += 1
	print nova_string


string = raw_input()
embaralha(string)

		
	
