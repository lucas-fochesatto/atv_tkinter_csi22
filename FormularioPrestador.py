import tkinter as tk
from tkinter import messagebox

from cep import buscar_cep


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
        self.janela.title(self.titulo())

        self.entries = {}
        for i, (label, attr) in enumerate(self.campos):
            tk.Label(self.janela, text=label).grid(row=i, column=0,
                                                   sticky="e", padx=5, pady=2)
            entry = tk.Entry(self.janela, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            entry.insert(0, self.valor_inicial(attr))
            self.entries[attr] = entry

        # ao sair do campo CEP, busca o endereço
        self.entries["cep"].bind("<FocusOut>", self.preencherEndereco)

        linha = len(self.campos)
        tk.Button(self.janela, text=self.texto_botao(),
                  command=self.salvar).grid(row=linha, column=1,
                                            sticky="e", padx=5, pady=8)

    def titulo(self):
        raise NotImplementedError

    def texto_botao(self):
        raise NotImplementedError

    def valor_inicial(self, attr):
        return ""

    def persistir(self, dados):
        raise NotImplementedError

    def preencherEndereco(self, event=None):
        cep = self.entries["cep"].get().strip()
        if not cep:
            return

        endereco = buscar_cep(cep)
        if endereco is None:
            return

        # para cada campo, limpar o conteúdo atual e depois inserir o novo.
        # preencher rua, bairro, cidade e uf usando o dict 'endereco'
        pass

    def salvar(self):
        dados = {attr: self.entries[attr].get() for _, attr in self.campos}
        sucesso, mensagem = self.persistir(dados)

        if sucesso:
            self.janela.destroy()
            if self.ao_salvar:
                self.ao_salvar()
            messagebox.showinfo("Prestador", mensagem)
        else:
            messagebox.showerror("Prestador", mensagem, parent=self.janela)
