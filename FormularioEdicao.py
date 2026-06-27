from FormularioPrestador import FormularioPrestador
from Prestador import Prestador


class FormularioEdicao(FormularioPrestador):
    # formulário em modo edição

    def __init__(self, parent, prestador, ao_salvar=None):
        self.prestador = prestador
        super().__init__(parent, ao_salvar=ao_salvar)

    def titulo(self):
        return "Editar Prestador"

    def texto_botao(self):
        return "Salvar"

    def valor_inicial(self, attr):
        return getattr(self.prestador, attr)

    def persistir(self, dados):
        mensagem = Prestador(id=self.prestador.id, **dados).updatePrestador()
        return mensagem.startswith("Prestador atualizado"), mensagem
