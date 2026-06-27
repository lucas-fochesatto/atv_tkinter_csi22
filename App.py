import tkinter as tk
from tkinter import ttk, messagebox

from Prestador import Prestador
from cep import buscar_cep


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
        FormularioPrestador(self.root, ao_salvar=self.carregarPrestadores)


class FormularioPrestador:

    campos = [
        ("Nome", "nome"),
        ("CPF ou CNPJ", "cpf_cnpj"),
        ("Data Nascimento", "data_nascimento"),
        ("CEP", "cep"),
        ("Rua", "rua"),
        ("Número", "numero"),
        ("Complemento", "complemento"),
        ("Bairro", "bairro"),
        ("Cidade", "cidade"),
        ("UF", "uf"),
        ("Contato", "contato"),
    ]

    def __init__(self, parent, ao_salvar=None):
        self.ao_salvar = ao_salvar
        self.janela = tk.Toplevel(parent)
        self.janela.title("Adicionar Prestador")

        self.entries = {}
        for i, (label, attr) in enumerate(self.campos):
            tk.Label(self.janela, text=label).grid(row=i, column=0,
                                                   sticky="e", padx=5, pady=2)
            entry = tk.Entry(self.janela, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[attr] = entry

        # gatilho do auto-preenchimento: ao sair do campo CEP, busca o endereço
        self.entries["cep"].bind("<FocusOut>", self.preencherEndereco)

        linha = len(self.campos)
        tk.Button(self.janela, text="Cadastrar",
                  command=self.cadastrar).grid(row=linha, column=1,
                                               sticky="e", padx=5, pady=8)

    def preencherEndereco(self, event=None):
        cep = self.entries["cep"].get().strip()
        if not cep:
            return  # campo vazio: não faz nada

        endereco = buscar_cep(cep)
        if endereco is None:
            return

        # para cada campo, limpar o conteúdo atual e depois inserir o novo.
        # preencher rua, bairro, cidade e uf usando o dict 'endereco'
        pass

    def cadastrar(self):
        dados = {attr: self.entries[attr].get() for _, attr in self.campos}
        prestador = Prestador(**dados)
        mensagem = prestador.insertPrestador()

        if mensagem.startswith("Prestador cadastrado"):
            self.janela.destroy()
            if self.ao_salvar:
                self.ao_salvar()
            messagebox.showinfo("Cadastro", mensagem)
        else:
            messagebox.showerror("Cadastro", mensagem, parent=self.janela)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
