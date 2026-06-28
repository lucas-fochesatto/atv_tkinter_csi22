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

    @staticmethod
    def listAll():
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""select id, nome, cpf_cnpj, cidade, uf, contato
                         from prestadores order by id desc""")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception:
            return []

    @staticmethod
    def buscarPorNome(nome):
        """
          - filtrar com o operador LIKE e o curinga %: where nome like ?
          - montar o parâmetro como  "%" + nome + "%"
          - pode ordenar por id desc, igual ao listAll
        """
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            # montar o SELECT das 6 colunas com WHERE nome LIKE ?

            # executar passando o parâmetro, ex.: c.execute(query, ("%" + nome + "%",))

            # pegar os resultados com c.fetchall()
            c.close()

            return []  # lista de linhas
        except Exception:
            return []

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
        except Exception as e:
            return f"Ocorreu um erro na inserção do prestador: {e}"

    def updatePrestador(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""update prestadores set
                         nome=?, cpf_cnpj=?, data_nascimento=?, rua=?,
                         numero=?, complemento=?, bairro=?, cidade=?,
                         uf=?, cep=?, contato=?
                         where id=?""",
                      (self.nome, self.cpf_cnpj, self.data_nascimento,
                       self.rua, self.numero, self.complemento, self.bairro,
                       self.cidade, self.uf, self.cep, self.contato, self.id))
            banco.conexao.commit()
            c.close()
            return "Prestador atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na atualização do prestador: {e}"


    def deletePrestador(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from prestadores where id=?", (self.id,))
            banco.conexao.commit()
            c.close()
            return "Prestador excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do prestador: {e}"
        
    def selectPrestador(self, id):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from prestadores where id=?", (id,))
            linha = c.fetchone()
            c.close()

            if linha:
                self.id = linha[0]
                self.nome = linha[1]
                self.cpf_cnpj = linha[2]
                self.data_nascimento = linha[3]
                self.rua = linha[4]
                self.numero = linha[5]
                self.complemento = linha[6]
                self.bairro = linha[7]
                self.cidade = linha[8]
                self.uf = linha[9]
                self.cep = linha[10]
                self.contato = linha[11]
                return "Busca realizada com sucesso!"
            else:
                return "Prestador não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do prestador: {e}"