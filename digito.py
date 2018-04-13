# coding: utf-8
# Aluna: Alice Fernandes Silva
# Digito verificador de 5 digitos
numero = raw_input()
numero1 = int(numero[0])
numero2 = int(numero[1])
numero3 = int(numero[2])
numero4 = int(numero[3])
numero5 = int(numero[4])
soma = numero1 + numero2 + numero3 + numero4 + numero5
numero_verificador = soma % 11.0
print "%s-%.2d" %(numero,numero_verificador)
