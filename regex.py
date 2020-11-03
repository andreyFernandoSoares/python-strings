import re

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

texto =  "Meu número para contato é 26133-5723 e 2225-5556"
retorno = re.search(padrao,texto)
print(retorno.group())

texto2 =  "Meu número para contato é 26133-5723 e 2225-5556"
retorno2 = re.findall(padrao,texto2)
print(retorno2)