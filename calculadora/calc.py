"""
Calculadora
"""

print("Seja bem vindo a calculadora simples!")


def somar(n1, n2):
    return (n1 + n2)

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

while True:
    choice = input("deseja somar, subtrair, multiplicar ou dividir?. (Caso queira sair, digite 'sair')\n")
        
    if choice == 'sair':
        print("Até a próxima vez!")
        break

    if choice in ['somar', 'multiplicar', 'subtrair', 'dividir']:
        try:        
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
        except ValueError:
            print("Por favor, digitar apenas números")
        
        if choice == 'somar':
            resultado = somar(n1, n2)

        elif choice == 'subtrair':
            resultado = subtrair(n1, n2)

        elif choice == 'multiplicar':
            resultado = multiplicar(n1, n2)

        elif choice == 'dividir':
            resultado = dividir(n1, n2)

        print(f"Resultado da operação {choice}: {resultado}")
        
    else:
        print("Operação não reconhecida. Por favor, escolha somar, subtrair, multiplicar ou dividir.")
        input("deseja somar, subtrair, multiplicar ou dividir?. (Caso queira sair, digite 'sair')\n")




