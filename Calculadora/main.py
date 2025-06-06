from tkinter import *

def botao(num):
    global texto_equacao

    texto_equacao = texto_equacao + str(num)
    espaco_equacao.set(texto_equacao)


def solucao():
    global texto_equacao
    
    try: 
        total = str(eval(texto_equacao))
        espaco_equacao.set(total)
        texto_equacao = total
    except ZeroDivisionError and SyntaxError:
        espaco_equacao.set('Erro')
        texto_equacao = ""


def limpar():
    global texto_equacao

    espaco_equacao.set("")
    texto_equacao = ""

# conversao de bases
def conversao_dec_bin():
    global texto_equacao
    try:
        numero_decimal = int(eval(texto_equacao))  
        binario = bin(numero_decimal)[2:]
        espaco_equacao.set(binario)
        texto_equacao = binario
    except Exception:
        espaco_equacao.set('Erro')
        texto_equacao = ""

def conversao_bin_dec(): 
    global texto_equacao
    try:
        numero_decimal = int(texto_equacao, 2)
        espaco_equacao.set(str(numero_decimal))
        texto_equacao = str(numero_decimal)
    except Exception:
        espaco_equacao.set("Erro")
        texto_equacao = ""


# configurações da janela: 
janela = Tk()
janela.title("Calculadora")
janela.geometry("400x500")
janela.config(background="#F3EBD8")

# espaço onde aparecem as equações: 
texto_equacao = ""
espaco_equacao = StringVar()

espaco = Label(janela, textvariable=espaco_equacao, font=20, width=25, height=4)
espaco.pack()

# configurações dos botões de número: 
quadro = Frame(janela)
quadro.config(background="#F3EBD8")
quadro.pack()

b1 = Button(quadro, text=1, height=2, width=6, font=35, 
            command=lambda: botao(1))
b1.config(bd=0)
b1.config(fg='#f9d0ce')
b1.config(bg='#f297a0')
b1.config(activebackground='#f9d0ce')
b1.config(activeforeground='#f297a0')

b1.grid(row=1, column=0)

b2 = Button(quadro, text=2, height=2, width=6, font=35, 
            command=lambda: botao(2))
b2.config(bd=0)
b2.config(fg='#f9d0ce')
b2.config(bg='#f297a0')
b2.config(activebackground='#f9d0ce')
b2.config(activeforeground='#f297a0')

b2.grid(row=1, column=1)

b3 = Button(quadro, text=3, height=2, width=6, font=35, 
            command=lambda: botao(3))
b3.config(bd=0)
b3.config(fg='#f9d0ce')
b3.config(bg='#f297a0')
b3.config(activebackground='#f9d0ce')
b3.config(activeforeground='#f297a0')

b3.grid(row=1, column=2)

b4 = Button(quadro, text=4, height=2, width=6, font=35, 
            command=lambda: botao(4))
b4.config(bd=0)
b4.config(fg='#f9d0ce')
b4.config(bg='#f297a0')
b4.config(activebackground='#f9d0ce')
b4.config(activeforeground='#f297a0')

b4.grid(row=2, column=0)

b5 = Button(quadro, text=5, height=2, width=6, font=35, 
            command=lambda: botao(5))
b5.config(bd=0)
b5.config(fg='#f9d0ce')
b5.config(bg='#f297a0')
b5.config(activebackground='#f9d0ce')
b5.config(activeforeground='#f297a0')

b5.grid(row=2, column=1)

b6 = Button(quadro, text=6, height=2, width=6, font=35, 
            command=lambda: botao(6))
b6.config(bd=0)
b6.config(fg='#f9d0ce')
b6.config(bg='#f297a0')
b6.config(activebackground='#f9d0ce')
b6.config(activeforeground='#f297a0')

b6.grid(row=2, column=2)

b7 = Button(quadro, text=7, height=2, width=6, font=35, 
            command=lambda: botao(7))
b7.config(bd=0)
b7.config(fg='#f9d0ce')
b7.config(bg='#f297a0')
b7.config(activebackground='#f9d0ce')
b7.config(activeforeground='#f297a0')

b7.grid(row=3, column=0)

b8 = Button(quadro, text=8, height=2, width=6, font=35, 
            command=lambda: botao(8))
b8.config(bd=0)
b8.config(fg='#f9d0ce')
b8.config(bg='#f297a0')
b8.config(activebackground='#f9d0ce')
b8.config(activeforeground='#f297a0')

b8.grid(row=3, column=1)

b9 = Button(quadro, text=9, height=2, width=6, font=35, 
            command=lambda: botao(9))
b9.config(bd=0)
b9.config(fg='#f9d0ce')
b9.config(bg='#f297a0')
b9.config(activebackground='#f9d0ce')
b9.config(activeforeground='#f297a0')

b9.grid(row=3, column=2)

b0 = Button(quadro, text=0, height=2, width=6, font=35, 
            command=lambda: botao(0))
b0.config(bd=0)
b0.config(fg='#f9d0ce')
b0.config(bg='#f297a0')
b0.config(activebackground='#f9d0ce')
b0.config(activeforeground='#f297a0')

b0.grid(row=4, column=1)

# configurações dos botões de operações: 
mais = Button(quadro, text='+', height=2, width=6, font=35, 
            command=lambda: botao('+'))
mais.config(bd=0)
mais.config(fg='#dbdebd')
mais.config(bg='#b6bb79')
mais.config(activebackground='#dbdebd')
mais.config(activeforeground='#b6bb79')

mais.grid(row=1, column=3)

menos = Button(quadro, text='-', height=2, width=6, font=35, 
            command=lambda: botao('-'))
menos.config(bd=0)
menos.config(fg='#dbdebd')
menos.config(bg='#b6bb79')
menos.config(activebackground='#dbdebd')
menos.config(activeforeground='#b6bb79')

menos.grid(row=2, column=3)

multiplicar = Button(quadro, text='*', height=2, width=6, font=35, 
            command=lambda: botao('*'))
multiplicar.config(bd=0)
multiplicar.config(fg='#dbdebd')
multiplicar.config(bg='#b6bb79')
multiplicar.config(activebackground='#dbdebd')
multiplicar.config(activeforeground='#b6bb79')

multiplicar.grid(row=3, column=3)

dividir = Button(quadro, text='/', height=2, width=6, font=35, 
            command=lambda: botao('/'))
dividir.config(bd=0)
dividir.config(fg='#dbdebd')
dividir.config(bg='#b6bb79')
dividir.config(activebackground='#dbdebd')
dividir.config(activeforeground='#b6bb79')

dividir.grid(row=4, column=3)

igual = Button(quadro, text='=', height=2, width=6, font=35, 
            command=solucao)
igual.config(bd=0)
igual.config(fg='#dbdebd')
igual.config(bg='#b6bb79')
igual.config(activebackground='#dbdebd')
igual.config(activeforeground='#b6bb79')

igual.grid(row=4, column=2)



deletar = Button(quadro, text='C', height=2, width=25, font=35, 
            command=limpar)
deletar.config(bd=0)
deletar.config(fg='#dbdebd')
deletar.config(bg='#b6bb79')
deletar.config(activebackground='#dbdebd')
deletar.config(activeforeground='#b6bb79')

deletar.grid(row=0, column=0, columnspan=4)

quadro1 = Frame(janela)
quadro1.config(background="#F3EBD8")
quadro1.pack()


b_conversao_dec_bin = Button(quadro1, text='Converter base decimal para base binária', 
                            command=conversao_dec_bin, height=2, width=40)
b_conversao_dec_bin.config(bd=0)
b_conversao_dec_bin.config(fg='#f9d0ce')
b_conversao_dec_bin.config(bg='#f297a0')
b_conversao_dec_bin.config(activebackground='#f9d0ce')
b_conversao_dec_bin.config(activeforeground='#f297a0')
b_conversao_dec_bin.grid(row=0, column=0)


b_conversao_bin_dec = Button(quadro1, text='Converter base binária para base decimal', 
                            command=conversao_bin_dec, height=2, width=40)
b_conversao_bin_dec.config(bd=0)
b_conversao_bin_dec.config(fg='#f9d0ce')
b_conversao_bin_dec.config(bg='#f297a0')
b_conversao_bin_dec.config(activebackground='#f9d0ce')
b_conversao_bin_dec.config(activeforeground='#f297a0')
b_conversao_bin_dec.grid(row=1, column=0)


janela.mainloop()