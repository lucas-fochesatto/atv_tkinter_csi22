import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('catalogo.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists prestadores(
                     id integer primary key autoincrement,
                     nome text,
                     cpf_cnpj text,
                     data_nascimento text,
                     rua text,
                     numero text,
                     complemento text,
                     bairro text,
                     cidade text,
                     uf text,
                     cep text,
                     contato text)""")
        self.conexao.commit()
        c.close()
