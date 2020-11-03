from extrator_argumentos import ExtratorArgumentosUrl

#SUBSTRING
sobre_mim = "Meu nome e Andrey e minha idade e 26"
idade = sobre_mim[34:37]
print(idade)

#BUSCAR
url = "moedaorigem=real"
index = url.find("=")
url_subs = url[index + 1:]
print(url_subs)


#SPLITZERA
lista_url = url.split("=")
print(lista_url)

#Extrator Argumentos
url1 = ExtratorArgumentosUrl("https://bytebank.com/moedaorigem=real&moedadestino=dolar&valor=500")

url2 = ExtratorArgumentosUrl("https://bytebank.com/moedaorigem=real&moedadestino=dolar&valor=1500")

print(id(url1))
print(id(url2))

#Equals
print(url1 == url2)

moeda_origem, moeda_destino = url2.extrai_argumentos()
valor = url2.extrai_valor()

print(url2)

#Replace
banco = "bytebank"

novobanco = banco.replace("byte", "andrey")
print(novobanco)
