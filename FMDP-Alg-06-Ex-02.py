'''2. Ordem decrescente. Escreva um programa Python que leia números inteiros (do usuário) e
os armazena em uma lista. Seu programa deve continuar lendo inteiros até que o usuário
entre com o valor 0 (zero). Então, o programa deve exibir em ordem decrescente todos os
números digitados pelo usuário sem incluir o valor 0, com um valor em cada linha impressa.'''

def descending_order(numbers):
    numbers.sort(reverse=True)  # Sort the numbers in descending order
    for num in numbers:
        print(num)  # Print each number in a separate line


def main():
    numbers = []
    while True:
        num = int(input("Enter an integer (0 to stop): "))
        if num == 0:
            break
        numbers.append(num)

    print("Numbers in descending order:")
    descending_order(numbers)

main()
