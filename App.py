import tkinter as tk
from tkinter import ttk, messagebox

from Prestador import Prestador
from FormularioCadastro import FormularioCadastro
from FormularioEdicao import FormularioEdicao


class App:

    # colunas exibidas na tabela
    COLUNAS = [
        ("id", "Id"),
        ("nome", "Nome"),
        ("cpf_cnpj", "CPF/CNPJ"),
        ("cidade", "Cidade"),
        ("uf", "UF"),
        ("contato", "Contato"),
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Prestadores de Serviço em TI")

        self.montarTabela()
        self.carregarPrestadores()

    def montarTabela(self):
        topo = tk.Frame(self.root)
        topo.pack(fill="x", padx=10, pady=10)

        tk.Button(topo, text="Adicionar Prestador",
                  command=self.abrirFormulario).pack(side="left")
        tk.Button(topo, text="Atualizar lista",
                  command=self.carregarPrestadores).pack(side="left", padx=5)
        tk.Button(topo, text="Editar",
                  command=self.editarSelecionado).pack(side="left", padx=(0, 5))
        tk.Button(topo, text="Excluir",
                  command=self.excluirSelecionado).pack(side="left")

        colunas = [c[0] for c in self.COLUNAS]
        self.tabela = ttk.Treeview(self.root, columns=colunas, show="headings")
        for col_id, titulo in self.COLUNAS:
            self.tabela.heading(col_id, text=titulo)
            self.tabela.column(col_id, width=120)
        self.tabela.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def carregarPrestadores(self):
        # limpa a tabela e recarrega do banco
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for linha in Prestador.listAll():
            self.tabela.insert("", "end", values=linha)

    def abrirFormulario(self):
        FormularioCadastro(self.root, ao_salvar=self.carregarPrestadores)

    def _idSelecionado(self):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showinfo("Atenção", "Selecione um prestador na tabela primeiro.")
            return None
        # o id é o primeiro valor da linha
        return self.tabela.item(selecao[0], "values")[0]

    def editarSelecionado(self):
        id = self._idSelecionado()
        if id is None:
            return
        prestador = Prestador()
        prestador.selectPrestador(id)
        FormularioEdicao(self.root, prestador, ao_salvar=self.carregarPrestadores)

    def excluirSelecionado(self):
        id = self._idSelecionado()
        if id is None:
            return
        if not messagebox.askyesno("Confirmar", "Excluir o prestador selecionado?"):
            return
        prestador = Prestador(id=id)
        mensagem = prestador.deletePrestador()
        self.carregarPrestadores()
        messagebox.showinfo("Excluir", mensagem)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
