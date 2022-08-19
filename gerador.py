from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Importando Pillow para adequar imagem de logo a janela 
from PIL import ImageTk, Image
# Importando Strings 
import string
# Para fazer a seleção aleatoria das chaves 
import random




co1 = '#0c0d0d' # Preto
co2 = '#f7fafa' # Branco
co3 = '#db0b19' # Vermelho
co4 = '#200bdb' # Azul

janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.config(bg=co2)

style = ttk.Style(janela)
style.theme_use('clam')


frame_cima = Frame(janela, width=295, height=50, bg=co2, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=co2, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando no Frame cima
img = Image.open('password.png') # Pegando a imagem 
img = img.resize((30, 30), Image.ANTIALIAS) # Definindo o tamanho da imagem
img = ImageTk.PhotoImage(img) # Deixando a imagem em um tamanho adequado para o tkinter 

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=co2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0,font='Ivy 16 bold', relief='flat', anchor='nw', bg=co2, fg=co1)
app_nome.place(x=36, y=2)

app_linha = Label(frame_cima, text='', width=295, height=1, padx=0,font='Ivy 1', relief='flat', anchor='nw', bg=co4, fg=co1)
app_linha.place(x=0, y=35)

# Função criar senha 
def criar_senha():
    alfa_maior = string.ascii_uppercase # Para letra maiscula
    alfa_menor = string.ascii_lowercase # Para letra minuscula 
    numero = '123456789'
    simbolos = '{}[]()*;/,_-'

    global combinar
    global senha 

    # Condição para Maiúscula 
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    
    else:
        pass
    
    # Condição para Minúscula  
    if estado_2.get() == alfa_menor:
        combinar += alfa_menor
    
    else:
        pass
    
     # Condição para números 
    if estado_3.get() == numero:
        combinar += numero
    
    else:
        pass

    # Condição para símbolos 
    if estado_4.get() == simbolos:
        combinar += simbolos
    
    else:
        pass


    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))
    

    app_senha['text'] = senha

def copiar_senha():
    global senha
    info = senha 
    frame_baixo.clipboard_clear()
    frame_baixo.clipboard_append(info)
    
    messagebox.showinfo("Sucesso","Senha copiada com sucesso")
    
botao_copiar= Button(frame_baixo,command=copiar_senha, text='Copiar',width=6, height=2, font='Ivy 10 bold', relief='flat', overrelief='solid', anchor='center', bg=co2, fg=co1)
botao_copiar.grid(row=0, column=1, sticky=NW, padx=2, pady=10, columnspan=1)


# Trabalhando no Frame baixo
app_senha = Label(frame_baixo, text='- - -', width=21, height=2, padx=0,  font='Ivy 12 bold', relief='solid', anchor='center', bg=co2, fg=co1)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)


app_info= Label(frame_baixo, text='Número total de caracteres na senha', height=1, padx=0,  font='Ivy 10 bold', relief='flat', anchor='nw', bg=co2, fg=co1)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar() # apenas para valores Inteiros 1, 2, 3
var.set(8) # Valor inicial que vai estar dentro da spinbox

spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var )
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=1)

alfa_maior = string.ascii_uppercase # Para letra maiscula
alfa_menor = string.ascii_lowercase # Para letra minuscula 
numero = '123456789'
simbolos = '{}[]()*;/,_-'


frame_caracter = Frame(frame_baixo, width=295, height=210, bg=co2, pady=0, padx=0, relief='flat')
frame_caracter.grid(row=3, column=0,columnspan=3, sticky=NSEW)


# Criando opção de letras maiuscúlas
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracter, width=1, var=estado_1, onvalue=alfa_maior, offvalue='off', relief='flat', bg=co2)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info= Label(frame_caracter, text='ABC Letras maiúsculas', height=1, padx=0,  font='Ivy 10 bold', relief='flat', anchor='nw', bg=co2, fg=co1)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# Criando opção de letra minuscula
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracter, width=1, var=estado_2, onvalue=alfa_menor, offvalue='off', relief='flat', bg=co2)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info= Label(frame_caracter, text='abc Letras minúsculas', height=1, padx=0,  font='Ivy 10 bold', relief='flat', anchor='nw', bg=co2, fg=co1)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# Criando a opção de números
estado_3 = StringVar()
estado_3.set(False)
check_2 = Checkbutton(frame_caracter, width=1, var=estado_3, onvalue=numero, offvalue='off', relief='flat', bg=co2)
check_2.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info= Label(frame_caracter, text='123 Números', height=1, padx=0,  font='Ivy 10 bold', relief='flat', anchor='nw', bg=co2, fg=co1)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

#Criando a opção de símbolos
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracter, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=co2)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info= Label(frame_caracter, text='!@# Símbolos', height=1, padx=0,  font='Ivy 10 bold', relief='flat', anchor='nw', bg=co2, fg=co1)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# Criando botão gerar senha
botao_senha= Button(frame_caracter, command=criar_senha, text='Gerar senha',width=35, height=1, font='Ivy 10 bold',overrelief='solid', relief='flat', anchor='center', bg=co4, fg=co2)
botao_senha.grid(row=5, column=0, columnspan=5 ,sticky=NSEW, padx=3, pady=18)


janela.mainloop()