#coding: utf-8
def somaImposto(taxaImposto, custo):
	imposto = custo * (taxaImposto/ 100.0)
	custo = custo + imposto
	return custo
