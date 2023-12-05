from tkinter import *
from tkinter import ttk
from tkinter import messagebox

agenda = [
    {"Nome": "Jonas", "Telefone": "85 98888-3333", "categoria":"Amigos"}
]

def atualizarTabela():
    for linha in tabela.get_children():
        tabela.delete()


def limparCampos():
    txtNome.delete(0, END)
    txtTelefone.delete(0, END)
    comboCategoria.set('')
def adicionarContato():
    nome = txtNome.get()
    telefone = txtTelefone.get()
    categoria = comboCategoria.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    agenda.append(contato)
    messagebox.showinfo('Sucesso!','Contato adicionado com sucesso!')
    atualizarTabela()
    limparCampos()

def tabelaClique(event):
    linhaSelecionada = tabela.selection()[0]
    global index
    index = tabela.index(linhaSelecionada)
    contato = agenda[index]
    limparCampos()
    txtNome.insert(0, contato['nome'])
    txtTelefone.insert(0, contato['telefone'])
    comboCategoria.set(contato['categoria'])

def editarContato():
    agenda[index] = {
        "nome": txtNome.get(),
        "telefone": txtTelefone.get(),
        "categoria": comboCategoria.get()
    }
    limparCampos()
    atualizarTabela()
    messagebox.showinfo('Sucesso!','Dados alterados com sucesso!')


def deletar():
    opcao = messagebox.askyesmo('Tem certeza?','Deseja remover o contato?')
    if opcao:
        agenda.remove(agenda[index])
        messagebox.showinfo('Sucesso!', 'Contato removido com sucesso!')
        limparCampos()
        atualizarTabela()

janela = Tk()
janela.title('Agenda Telefonica')

labelNome = Label(janela, text='Nome:', fg='navy', font='Tahoma 14 bold')
labelNome.grid(row=0, column=0)

txtNome = Entry(janela, font='Tahoma 14', width=27)
txtNome.grid(row=0, column=1)

labelTelefone = Label(janela, text='Telefone:', fg='navy', font='Tahoma 14 bold')
labelTelefone.grid(row=1, column=0)

txtTelefone = Entry(janela, font='Tahoma 14', width=27)
txtTelefone.grid(row=1, column=1)

labelCategoria = Label(janela, text='Categoria:', fg='navy', font='Tahoma 14 bold')
labelCategoria.grid(row=2, column=0)

categorias = ['Amigos', 'Trabalho', 'Familia']
comboCategoria = ttk.Combobox(janela, values=categorias, font='Tahoma 14', width=25)
comboCategoria.grid(row=2, column=1)

btnAdicionar = Button(janela, text='Adcionar', fg='navy', bg='white',
                      font='Tahoma 12 bold', width=8, command=adicionarContato)
btnAdicionar.grid(row=3, column=0)

btnEditar = Button(janela, text='Editar', fg='navy', bg='white',
                   font='Tahoma 12 bold', width=8)
btnEditar.grid(row=3, column=1)

btnRemover = Button(janela, text='Remover', fg='navy', bg='white',
                    font='Tahoma 12 bold', width=8, command=deletar)
btnRemover.grid(row=3, column=2)

# Como criar uma tabela (TreeView)
colunas = ['Nome', 'Telefone', 'Categoria']
tabela = ttk.Treeview(janela, columns=colunas, show='headings')
# show=headings -> Oculta a coluna com o id da linha
for coluna in colunas:
    # Renomeando a coluna
    tabela.heading(coluna, text=coluna)
tabela.grid(row=4, columnspan=3)

tabela.bind('<ButtonRelease-1>', tabelaClique)




atualizarTabela()
janela.mainloop()
