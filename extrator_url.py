class ExtratorURL:
    def __init__(self, url):
        self.url = self.santiza_url(url)
        self.valida_url()

    def santiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia")






extrator_url = ExtratorURL("  ")
#extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dollar&quantidade=100")
#valor_quantidade = extrator_url.get_valor_parametro("quantidade")