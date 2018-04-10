# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Valor de passagem aérea

distancia = float(raw_input())
valor_aliquota = float(raw_input())
valor_passagem = distancia * valor_aliquota + 51.00
valor_vista = valor_passagem - 25/100.0 * valor_passagem
valor_parcelado = valor_passagem * 0.95
valor_parcelado1 = valor_parcelado / 6.0
valor_parcelado2 = valor_passagem / 10.0

print "Valor da passagem: R$ %.2f" %(valor_passagem)
print
print "Pagamento:"
print "1. À vista. R$ %.2f" %(valor_vista)
print "2. Em 6 parcelas. Total: R$ %.2f" %(valor_parcelado)
print "   6 x R$ %.2f" %(valor_parcelado1)
print "3. Em 10 parcelas. Total: R$ %.2f" %(valor_passagem)
print "   10 x R$ %.2f" %(valor_parcelado2)
