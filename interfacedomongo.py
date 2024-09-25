import tkinter as tk
from tkinter import messagebox
import cruddomongo as crud 

def criar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome and telefone:
        resultado = crud.criar_contato(nome, telefone, email)
        messagebox.showinfo("Sucesso", resultado)
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        listar_contatos()
    else:
        messagebox.showwarning("Erro", "Nome e Telefone são obrigatórios!")

def listar_contatos():
    contatos = crud.listar_contatos()
    text_contatos.delete('1.0', tk.END)
    for contato in contatos:
        text_contatos.insert(tk.END, contato + '\n')

def atualizar_contato():
    nome = entry_nome.get()
    novo_telefone = entry_telefone.get()
    novo_email = entry_email.get()

    if nome:
        resultado = crud.atualizar_contato(nome, novo_telefone, novo_email)
        messagebox.showinfo("Resultado", resultado)
        listar_contatos()
    else:
        messagebox.showwarning("Erro", "Nome do contato a ser atualizado é obrigatório!")

def deletar_contato():
    nome = entry_nome.get()

    if nome:
        resultado = crud.deletar_contato(nome)
        messagebox.showinfo("Resultado", resultado)
        listar_contatos()
    else:
        messagebox.showwarning("Erro", "Nome do contato a ser deletado é obrigatório!")

window = tk.Tk()
window.title("Gerenciamento de Contatos")
window.geometry("500x450")
window.configure(bg="#f0f0f0")

label_style = {"font": ("Arial", 12), "bg": "#f0f0f0"}
entry_style = {"font": ("Arial", 12), "bd": 2, "relief": "solid"}
button_style = {"font": ("Arial", 10, "bold"), "bg": "#4CAF50", "fg": "white", "bd": 0, "relief": "flat"}
text_style = {"font": ("Arial", 12), "bd": 2, "relief": "solid", "bg": "#f9f9f9", "fg": "#333"}

frame_inputs = tk.Frame(window, bg="#f0f0f0")
frame_inputs.pack(pady=10)

label_nome = tk.Label(frame_inputs, text="Nome:", **label_style)
label_nome.grid(row=0, column=0, sticky="w", padx=10)

entry_nome = tk.Entry(frame_inputs, **entry_style)
entry_nome.grid(row=0, column=1, padx=10)

label_telefone = tk.Label(frame_inputs, text="Telefone:", **label_style)
label_telefone.grid(row=1, column=0, sticky="w", padx=10)

entry_telefone = tk.Entry(frame_inputs, **entry_style)
entry_telefone.grid(row=1, column=1, padx=10)

label_email = tk.Label(frame_inputs, text="Email (Opcional):", **label_style)
label_email.grid(row=2, column=0, sticky="w", padx=10)

entry_email = tk.Entry(frame_inputs, **entry_style)
entry_email.grid(row=2, column=1, padx=10)

frame_buttons = tk.Frame(window, bg="#f0f0f0")
frame_buttons.pack(pady=10)

btn_criar = tk.Button(frame_buttons, text="Criar Contato", **button_style, command=criar_contato)
btn_criar.grid(row=0, column=0, padx=10, pady=5)

btn_listar = tk.Button(frame_buttons, text="Listar Contatos", **button_style, command=listar_contatos)
btn_listar.grid(row=0, column=1, padx=10, pady=5)

btn_atualizar = tk.Button(frame_buttons, text="Atualizar Contato", **button_style, command=atualizar_contato)
btn_atualizar.grid(row=1, column=0, padx=10, pady=5)

btn_deletar = tk.Button(frame_buttons, text="Deletar Contato", **button_style, command=deletar_contato)
btn_deletar.grid(row=1, column=1, padx=10, pady=5)

frame_contatos = tk.Frame(window, bg="#f0f0f0")
frame_contatos.pack(pady=10)

label_contatos = tk.Label(frame_contatos, text="Contatos:", **label_style)
label_contatos.pack(anchor="w", padx=10)

text_contatos = tk.Text(frame_contatos, height=8, **text_style)
text_contatos.pack(fill="x", padx=10, pady=5)

window.mainloop()
