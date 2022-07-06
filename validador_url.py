import re

class ValidadorUrl:
    def __init__(self, url):
        self.url = url

    def valida(self):
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            return False
        else:
            return True