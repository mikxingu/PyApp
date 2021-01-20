from tkinter import *
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master) #Cria o widget1 e atribui ele ao nosso container top-level(master)
        self.widget1.pack(side=RIGHT) #Faz o pack do widget1
        self.msg = Label(self.widget1, text="Primeiro Widget") # Cria uma item msg que atribui uma string a janela widget1
        self.msg["font"] = ("Verdana", "10", "italic", "bold") # Configuracoes visuais da string
        self.msg.pack() 
        self.sair = Button(self.widget1) # cria um botao na widget1
        self.sair["text"] = "Sair" #texto do botao "sair"
        self.sair["font"] = ("Calibri", "10") 
        self.sair["width"] = 5 #tamanho do botao
        self.sair["command"] = self.widget1.quit #comando executado ao clicar no botao
        self.sair.pack(side=RIGHT)
root = Tk()
Application(root)
root.mainloop()