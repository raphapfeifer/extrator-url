import re

endereco = "Rua das Bandeiras, apartamento 131, Santo André, SP, 09090-780"

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)