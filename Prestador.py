from Banco import Banco

class Prestador(object):
    def __init__(self, id=0, nome="", cpf_cnpj="", data_nascimento="",
                 rua="", numero="", complemento="", bairro="", cidade="",
                 uf="", cep="", contato=""):
        self.id = id
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.data_nascimento = data_nascimento
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.contato = contato

    def insertPrestador(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""insert into prestadores
                         (nome, cpf_cnpj, data_nascimento, rua, numero,
                          complemento, bairro, cidade, uf, cep, contato)
                         values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (self.nome, self.cpf_cnpj, self.data_nascimento,
                       self.rua, self.numero, self.complemento, self.bairro,
                       self.cidade, self.uf, self.cep, self.contato))
            banco.conexao.commit()
            c.close()
            return "Prestador cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do prestador"

    def updatePrestador(self):
        pass

    def deletePrestador(self):
        pass

    def selectPrestador(self, id):
        pass