url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dollar&quantidade=100"
#print(url)

#url = 'bytebank.com/cambio?moedaOrigem=real'


#separa base e os parametros
indice_interrogacao = url.find('?')
print('Esse é o ínice: {}'.format(indice_interrogacao))
url_base = url[0:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao +1:]
print(url_parametros)




# Busca o valor de um parametro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
