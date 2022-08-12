from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# cores 
co0 = "#f0f3f5" # preto
co1 = "#feffff" # branco
co2 = "#1751e3" # azul
co3 = "#38576b" # valor
co4 = "#403d3d" # fonte

# criando janela
janela = Tk()
janela.title('Login')
janela.geometry('310x300') # comprimento da interface
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE) 

# dividindo  janela 
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NS)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW) 

# configurando frame up
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5) 

l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45) 

# função para criar acesso e erro
credenciais = ['Iago', '12345678']

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'adm' and senha == 'adm':
        messagebox.showinfo('Login', 'Seja bem vindo Admin !!!')
    
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo(f'Login', 'Seja bem vindo ' +credenciais[0])
        
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_aba()

    else:
        messagebox.showwarning('Erro', 'Usuário ou senha incorretos !')

# função após acesso / erro
def nova_aba():

    l_nome = Label(frame_cima, text='Usuário: ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5) 

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja bem vindo ' +credenciais[0], anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=10, y=105)    

#configurando frame down
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20) 
e_nome = Entry(frame_baixo, width=25, justify='left', font=(", 15"), highlightthickness=1, relief="solid" )
e_nome.place(x=14, y=50) 

l_pass = Label(frame_baixo, text='Password *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95) 
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=(", 15"), highlightthickness=1, relief="solid" )
e_pass.place(x=14, y=130) 

l_confirm = Button(frame_baixo,command=verificar_senha, text='Enter',width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
l_confirm.place(x=15, y=180)


janela.mainloop()
            
