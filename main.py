from extrator_url import ExtratorURL

extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dollar&quantidade=100")
#extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")


print("O tamanho da url: ", len(extrator_url))


print(valor_quantidade)