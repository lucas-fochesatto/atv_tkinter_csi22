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
        # Montagem da URL
        url = f"https://viacep.com.br/ws/{cep}/json/"

        #requisição HTTP via urllib 
        with urllib.request.urlopen(url) as response:
            resposta = response.read()

        #conversão de bytes JSON para dicionário Python
        dados = json.loads(resposta)

        # Verificação se o CEP existe
        if dados.get("erro"):
            return None

        #adaptando para o nosso sistema o que a API devolve
        return {
            "rua": dados.get("logradouro", ""),
            "bairro": dados.get("bairro", ""),
            "cidade": dados.get("localidade", ""),
            "uf": dados.get("uf", "")
        }

    except Exception as e:
        print(f"[Debug] Falha na requisição ViaCEP: {e}")
        return None