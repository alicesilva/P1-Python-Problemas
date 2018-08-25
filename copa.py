#coding: utf-8

def joga_em(pais, cidade, grupos, estadios):
	valor = grupos.get("A")
	print valor

grupos = {"A":["Brasil","Croácia", "México","Camarões"],
		  "B":["Espanha", "Holanda", "Chile", "Austrália"],
		  "C":["Colômbia", "Grécia", "Costa do Marfim", "Japão"],
		"D":["Uruguai", "Costa Rica", "Inglaterra", "Austrália"],
"E":["Suiça", "Equador", "França", "Honduras", ],
"F":["Argentina", "Bósnia", "Irã", "Nigéria"],
"G":["Alemanha", "Portugal", "Gana", "Estados Unidos"],
"H":["Bélgica", "Argélia", "Rússia", "Córeia do Sul"]
}
estadios = {("A","B"): ["Belo Horizonte", "Fortaleza", "Salvador"],
("C","D"): ["Rio de Janeiro", "Recife", "Fortaleza", "Salvador"],
("E","F"): ["Brasília", "São Paulo", "Rio de Janeiro"],
("G","H"): ["Porto Alegre", "Salvador", "Rio de Janeiro", "Brasília"]
}
joga_em("Croácia", "Fortaleza", grupos, estadios)
joga_em("Alemanha", "Porto Alegre", grupos, estadios)
joga_em("Brasil", "Brasília", grupos, estadios)
