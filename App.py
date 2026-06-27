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

    def __init__(self, parent, ao_salvar=None, prestador=None):
        self.ao_salvar = ao_salvar
        # prestador None = modo cadastro; com objeto = modo edição
        self.prestador = prestador
        self.modo_edicao = prestador is not None

        self.janela = tk.Toplevel(parent)
        self.janela.title("Editar Prestador" if self.modo_edicao
                          else "Adicionar Prestador")

        self.entries = {}
        for i, (label, attr) in enumerate(self.campos):
            tk.Label(self.janela, text=label).grid(row=i, column=0,
                                                   sticky="e", padx=5, pady=2)
            entry = tk.Entry(self.janela, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[attr] = entry

            # em modo edição, pré-preenche cada campo com o valor atual
            if self.modo_edicao:
                entry.insert(0, getattr(self.prestador, attr))

        # gatilho do auto-preenchimento: ao sair do campo CEP, busca o endereço
        self.entries["cep"].bind("<FocusOut>", self.preencherEndereco)

        linha = len(self.campos)
        texto_botao = "Salvar" if self.modo_edicao else "Cadastrar"
        tk.Button(self.janela, text=texto_botao,
                  command=self.salvar).grid(row=linha, column=1,
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

    def salvar(self):
        dados = {attr: self.entries[attr].get() for _, attr in self.campos}

        if self.modo_edicao:
            # mantém o id do prestador em edição e atualiza
            prestador = Prestador(id=self.prestador.id, **dados)
            mensagem = prestador.updatePrestador()
            sucesso = mensagem.startswith("Prestador atualizado")
        else:
            prestador = Prestador(**dados)
            mensagem = prestador.insertPrestador()
            sucesso = mensagem.startswith("Prestador cadastrado")

        if sucesso:
            self.janela.destroy()
            if self.ao_salvar:
                self.ao_salvar()
            messagebox.showinfo("Prestador", mensagem)
        else:
            messagebox.showerror("Prestador", mensagem, parent=self.janela)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
