'''14. Precedência de operadores. Escreva uma função chamada precedencia que retorna um
inteiro representando a precedência de um operador matemático. Uma string contendo o
operador será passada para a função como seu único parâmetro. Sua função deve retornar 1
para + e -, 2 para * e / e 3 para ^. Se a string passada para a função não for um desses
operadores, a função deve retornar -1. Inclua um programa principal que lê um operador do
usuário e exibe a precedência do operador ou uma mensagem de erro indicando que a
entrada não era um operador.

Observação: Neste exercício, junto com outros que aparecem posteriormente nesta lista,
usaremos ^ para representar a exponenciação. Usar ^ ao invés do operador ** do Python
tornará esses exercícios mais fáceis porque um operador sempre será um único caractere.'''

def precedencia(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/':
        return 2
    elif operador == '^':
        return 3
    else:
        return -1

def main():
    operador = input("Digite um operador matemático (+, -, *, /, ^): ")
    valor_precedencia = precedencia(operador)
    if valor_precedencia == -1:
        print("Erro: entrada inválida! O valor digitado não é um operador válido.")
    else:
        print(f"A precedência do operador {operador} é: {valor_precedencia}")

main()
