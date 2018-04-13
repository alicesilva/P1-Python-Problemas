# coding: utf-8
# Aluna: Alice Fernandes Silva
# Tweests por página
quant = int(raw_input())
if quant < 400:
	print "Serão necessárias 0 página(s) para visualizar os tweets."
	print "100.0% dos tweets serão perdidos."
else:
	paginas = quant / 400
	percentual_perdido = ((quant-400) / float(quant)) * 100
	print "Serão necessárias %d página(s) para visualizar os tweets." %(paginas)
	print "%.1f%% dos tweets serão perdidos." %(percentual_perdido)
