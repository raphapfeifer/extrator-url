url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dollar&quantidade=100"
#print(url)

#url = 'bytebank.com/cambio?moedaOrigem=real'

indice_interrogacao = url.find('?')
print('Esse é o ínice: {}'.format(indice_interrogacao))
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao +1:]
print(url_parametros)

#x = int(url.find('?'))
#print(x)
#resultado = ['Caractere encontrado', 'Caractere não encontrado'][x > 0]
#print(resultado)



parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)

print(indice_parametro)


indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:16]
print(valor)
