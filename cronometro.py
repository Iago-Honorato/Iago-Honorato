from tkinter import *


# Cores 
co1 = '#020302' # Preto
co2 = '#f2faf4' # Branco
co3 = '#047d06' # Verde
co4 = '#9e050a' # Vermelho
co5 = '#6c6d70' # Cinza
co6 = '#031c80' # Azul

# Criando Janela
janela = Tk()
janela.title('Time')
janela.geometry('300x180')
janela.config(bg=co1)
janela.resizable(width=False, height=False)

global tempo
global rodar 
global contador
global limitador

tempo = "00:00:00"
rodar = False
contador = -5
limitador = 59

# Função Iniciar
def iniciar():
    global contador
    global tempo
    global limitador
    
    if rodar:
        # Contagem antes do cronometro startar
        if contador <= -1:
            inicio = 'INICIAR EM  ' +str(contador).replace('-', '')
            label_time['text'] = inicio
            label_time['font'] = 'Arial 30 bold'
        # Rodando o cronômetro
        else:
            label_time['font'] = 'Times 50 bold'
            temporaria = str(tempo)
            h,m,s = map(int, temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)
             
            if (s>= limitador):
                contador = 0
                m += 1
            
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            # Atualizando os valores atuais 
            temporaria = str(h[-2:])+':'+str(m[-2:])+':'+str(s[-2:])
            label_time['text'] = temporaria
            tempo = temporaria


        label_time.after(1000, iniciar)
        contador += 1

# Função para começar
def start():
    global rodar
    global contador
    rodar = True
    iniciar() 

# Função para parar
def pausar():
    global rodar
    rodar = False

# Função para recomeçar
def reiniciar():
    global tempo
    global contador 

    # Reiniciando o contador 
    contador = 0
    tempo = "00:00:00"
    label_time['text'] = tempo
   

# Criando Labels
label_app = Label(janela, text='Cronômetro', font='Arial 10', bg=co1, fg=co2)
label_app.place(x=20, y=5)

label_time= Label(janela, text=tempo, font='times 50 bold', bg=co1, fg=co6)
label_time.place(x=20, y=30)

# Criando Botões 
botao_iniciar = Button(janela,command=start, text='Iniciar', width=10, height=2, bg=co1, fg=co2, font='Ivy 8 bold', relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar,text='Pausar', width=10, height=2, bg=co1, fg=co2, font='Ivy 8 bold', relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=co1, fg=co2, font='Ivy 8 bold', relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)



janela.mainloop()