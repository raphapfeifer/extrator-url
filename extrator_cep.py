import re

endereco = "Rua das Bandeiras, apartamento 131, Santo André, SP, 09090-780"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)