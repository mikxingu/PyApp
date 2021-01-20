from tkinter import *
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master) #Cria o widget1 e atribui ele ao nosso container top-level(master)
        self.widget1.pack() #Faz o pack do widget1
        self.msg = Label(self.widget1, text="Primeiro widget") # Cria uma item msg que atribui uma string a janela widget1
        self.msg["font"] = ("Calibri", "9", "italic") # Configuracoes visuais da string
        self.msg.pack() 
        self.sair = Button(self.widget1) # cria um botao na widget1
        self.sair["text"] = "Clique aqui" #texto do botao "sair"
        self.sair["font"] = ("Calibri", "9") 
        self.sair["width"] = 10 #tamanho do botao
        self.sair["command"] = self.mudarTexto
        self.sair.pack()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

root = Tk()
Application(root)
root.mainloop()