# Console Calculator made using python.

import this
self = this

# Functions

def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

quitapp = True

while (quitapp):
    print("Bem vindo a calculadora python.")
    print("Escolha uma das opcoes: ")
    print("1-Soma | 2-Subtracao | 3-Multiplicacao | 4-Divisao | q-Sair.")
    opt = input("Opção: ")
    if (opt == "1"):
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = sum(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    if (opt == "2"):
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = subtract(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    if (opt == "3"):
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = multiply(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    if (opt == "4"):
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = divide(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    if (opt == "q"):
        print("Obrigado! Até logo.")
        quitapp = False
        quit(self)
    
    else:
        print("Opção inválida.")
        print()
    
