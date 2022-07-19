from extrator_url import ExtratorURL


url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dollar&quantidade=100"
extrator_url = ExtratorURL(url)
#extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")


print("O tamanho da url: ", len(extrator_url))

print(extrator_url)


print(valor_quantidade)

extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print(id(extrator_url))
print(id(extrator_url_2))

#print(extrator_url == extrator_url_2)