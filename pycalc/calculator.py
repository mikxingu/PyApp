# Console Calculator made using python.


# Functions

import this

def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

self = this

print("Bem vindo a calculadora python.")
print("Escolha uma das opcoes: ")
print("1-Soma | 2-Subtracao | 3-Multiplicacao | 4-Divisao | Q-Sair.")

opt = input("Opção: ")

if (opt == "1"):
    inputx = float(input("Informe o primeiro valor: "))
    inputy = float(input("Informe o segundo valor: "))
    output = sum(inputx, inputy)
    print(output)

if (opt == "2"):
    inputx = float(input("Informe o primeiro valor: "))
    inputy = float(input("Informe o segundo valor: "))
    output = subtract(inputx, inputy)
    print(output)

if (opt == "3"):
    inputx = float(input("Informe o primeiro valor: "))
    inputy = float(input("Informe o segundo valor: "))
    output = multiply(inputx, inputy)
    print(output)

if (opt == "4"):
    inputx = float(input("Informe o primeiro valor: "))
    inputy = float(input("Informe o segundo valor: "))
    output = divide(inputx, inputy)
    print(output)

# if (opt == "Q" or "q"):
#     print("Obrigado! Até logo.")
#     quit(self)

