def _digitos(texto):
    # mantém só os caracteres numéricos
    return "".join(caractere for caractere in texto if caractere.isdigit())


def mascara_cpf_cnpj(texto):
    """
    Adaptativa:
      até 11 dígitos -> CPF   000.000.000-00
      de 12 a 14     -> CNPJ  00.000.000/0000-00
    """
    d = _digitos(texto)[:14]
    if len(d) <= 11:
        return _formatar_cpf(d)
    return _formatar_cnpj(d)


def _formatar_cpf(d):
    # d tem de 0 a 11 dígitos
    if len(d) <= 3:
        return d
    if len(d) <= 6:
        return d[:3] + "." + d[3:]
    if len(d) <= 9:
        return d[:3] + "." + d[3:6] + "." + d[6:]
    return d[:3] + "." + d[3:6] + "." + d[6:9] + "-" + d[9:]


def _formatar_cnpj(d):
    # d tem de 12 a 14 dígitos
    saida = d[:2] + "." + d[2:5] + "." + d[5:8] + "/" + d[8:12]
    if len(d) > 12:
        saida += "-" + d[12:]
    return saida


def mascara_data(texto):
    # TODO: implementar
    return texto


def mascara_cep(texto):
    # TODO: implementar
    return texto
