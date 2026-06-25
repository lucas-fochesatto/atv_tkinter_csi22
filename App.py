import tkinter as tk
from tkinter import messagebox
from Prestador import Prestador

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Prestadores de Serviço em TI")

        # campos do formulário
        self.campos = [
            ("Nome", "nome"),
            ("CPF ou CNPJ", "cpf_cnpj"),
            ("Data Nascimento", "data_nascimento"),
            ("Rua", "rua"),
            ("Número", "numero"),
            ("Complemento", "complemento"),
            ("Bairro", "bairro"),
            ("Cidade", "cidade"),
            ("UF", "uf"),
            ("CEP", "cep"),
            ("Contato", "contato"),
        ]

        self.entries = {}
        self.montarFormulario()

    def montarFormulario(self):
        for i, (label, attr) in enumerate(self.campos):
            tk.Label(self.root, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=2)
            entry = tk.Entry(self.root, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[attr] = entry

        linha = len(self.campos)
        tk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=linha, column=1, sticky="e", padx=5, pady=8)

    def cadastrar(self):
        dados = {attr: self.entries[attr].get() for _, attr in self.campos}
        prestador = Prestador(**dados)
        mensagem = prestador.insertPrestador()
        messagebox.showinfo("Cadastro", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
