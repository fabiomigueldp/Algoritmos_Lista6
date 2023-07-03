'''1. Ordem Crescente. Escreva um programa Python que leia números inteiros (do usuário) e os
armazena em uma lista. Seu programa deve continuar lendo inteiros até que o usuário entre
com o valor 0 (zero). Então, o programa deve exibir em ordem crescente todos os números
digitados pelo usuário sem incluir o valor 0, com um valor em cada linha impressa. Obs.: você
pode implementar o algoritmo de ordenação BubbleSort ou usar o método sort ou a função
sorted para ordenar a lista.'''

def ascending_order(numbers):
    numbers.sort()
    for num in numbers:
        print(num)


def main():
    numbers = []
    while True:
        num = int(input("Enter an integer (0 to stop): "))
        if num == 0:
            break
        numbers.append(num)

    print("Numbers in ascending order:")
    ascending_order(numbers)

main()
