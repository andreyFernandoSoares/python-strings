class ExtratorArgumentosUrl:

    def __init__(self, url):
        if (self.valida_url(url)):
            self.__url = url.lower()
        else:
            raise LookupError("Url Invalida!!!")
    
    @staticmethod
    def valida_url(url):
        if url:
            return url.startswith("https://bytebank.com")
        else:
            return False
    
    def __len__(self):
        len(self.__url)
    
    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        representacao = "Valor: {}\nMoeda Origem: {}\nMoeda Destino: {}\n".format(self.extrai_valor(), moeda_origem, moeda_destino)
        return representacao
    
    def __eq__(self, outra_instancia):
        return self.__url == outra_instancia.url
    
    def extrai_argumentos(self):
        busca_moeda_origem = "moedaorigem="
        busca_moeda_destino = "moedadestino="

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_final_moeda_destino = self.__url.find("&valor")

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.__url.find("&")

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.__url.find("&")

        moeda_destino = self.__url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino
    
    def encontra_indice_inicial(self, moeda_buscada):
        return self.__url.find(moeda_buscada) + len(moeda_buscada)
    
    def troca_moeda_origem(self):
        self.__url = self.__url.replace("moedadestino", "real", 1)
    
    @property
    def url(self):
        return self.__url

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)
        valor = self.__url[indice_inicial_valor:]
        return valor