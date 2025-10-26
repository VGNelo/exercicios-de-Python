import tkinter  # apenas um espaço aqui

janela = tkinter.Tk()
label = tkinter.Label(janela, text='Isso é uma interface gráfica simples!')
label.pack()

janela.mainloop()  # melhor usar o método da instância
