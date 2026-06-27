"""
Consulta de CEP na API pública ViaCEP.
a função recebe um CEP (string)
e deve devolver um dicionário com as chaves: rua, bairro, cidade, uf
ou None se algo der errado
"""
import json
import urllib.request


def buscar_cep(cep):
    # mantém só os dígitos: "01001-000" -> "01001000"
    cep = "".join(caractere for caractere in cep if caractere.isdigit())

    if len(cep) != 8:
        return None

    try:
        # monte a URL no formato: https://viacep.com.br/ws/<cep>/json/
        url = ""

        # fazer a requisição e ler a resposta em bytes
        # urllib.request.urlopen(url) e depois .read()
        resposta = b"{}"

        # converter os bytes JSON em um dicionário Python
        # json.loads(...)
        dados = {}

        if dados.get("erro"):
            return None

        # As chaves da ViaCEP são diferentes das nossas:
        #   logradouro -> rua
        #   bairro     -> bairro
        #   localidade -> cidade
        #   uf         -> uf

        # montar e retorne o dicionário no NOSSO formato
        return {}

    except Exception:
        # Sem internet, timeout, resposta inesperada... não preenche nada
        return None
