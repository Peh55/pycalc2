from tkinter import *
#Classe que inivis a interface gráfica

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        #O còdigo acima cria o cantainer mãe que receberá outro

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        #Bloco do segundo container

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        #Bloco do terceiro container

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        # Bloco do quarto container

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()
        # Bloco do quinto container

        self.titulo = Label(self.primeiroContainer, text="Calculadora")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        #Etiqueta que mostra a palavra Número 1 ele sera embutido no segundo container

        self.n1 = Entry(self.segundoContainer)
        self.n1["width"] = 30
        self.n1["font"] = self.fontePadrao
        self.n1.pack(side=LEFT)

        self.n2Label = Label(self.terceiroContainer, text="Número 02", font=self.fontePadrao)
        self.n2Label.pack(side=LEFT)

        self.n2 = Entry(self.terceiroContainer)
        self.n2["width"] = 30
        self.n2["font"] = self.fontePadrao
        self.n2.pack(side=LEFT)

        self.soma = Button(self.quartoContainer)
        self.soma["text"] = "somar"
        self.soma["font"] = ("Calibri", "8")
        self.soma["width"] = 12
        self.soma["command"] = self.somar
        self.soma.pack(side=LEFT)

        self.sub = Button(self.quartoContainer)
        self.sub["text"] = "Subtrair"
        self.sub["font"] = ("Calibri", "8")
        self.sub["width"] = 12
        self.sub["command"] = self.subtrair
        self.sub.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        def somar(self):
            global resultado
            num1 = self.n1.get()
            num2 = self.n2.get()
            convert = float(num1) + float(num2)
            resultado = str(convert)
            self.mensagem["text"] = resultado

        def subtrair(self):...

root = Tk()
Application(root)
root.mainloop()