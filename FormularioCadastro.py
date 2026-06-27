from FormularioPrestador import FormularioPrestador
from Prestador import Prestador


class FormularioCadastro(FormularioPrestador):
    # formulário em modo cadastro

    def titulo(self):
        return "Adicionar Prestador"

    def texto_botao(self):
        return "Cadastrar"

    def persistir(self, dados):
        mensagem = Prestador(**dados).insertPrestador()
        return mensagem.startswith("Prestador cadastrado"), mensagem
