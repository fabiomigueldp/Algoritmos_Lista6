'''3. Removendo extremos. Ao analisar os dados coletados como parte de um experimento
científico, pode ser desejável remover os valores mais extremos antes de realizar outros
cálculos. Escreva uma função que tenha uma lista de valores e um número inteiro não
negativo, n, como seus parâmetros. A função deve criar uma nova cópia da lista com os n
maiores elementos e os n menores elementos removidos. Em seguida, ele deve retornar a
nova cópia da lista como o único resultado da função. A ordem dos elementos na lista
retornada não precisa coincidir com a ordem dos elementos na lista original.
Escreva um programa principal que demonstre sua função. Sua função main deve ler uma lista
de números do usuário e remover os dois maiores e os dois menores valores dela. Exiba a
lista com os extremos removidos, seguido pela lista original. Seu programa deve gerar uma
mensagem de erro apropriada se o usuário inserir menos de 4 valores.'''

def remove_extremes(numbers, n):
    if len(numbers) < 4:
        raise ValueError("Error: The list should contain at least 4 values.")

    sorted_numbers = sorted(numbers)
    new_list = sorted_numbers[n:len(sorted_numbers)-n]
    return new_list


def main():
    try:
        numbers = []
        while True:
            num = int(input("Enter a number (0 to stop): "))
            if num == 0:
                break
            numbers.append(num)

        removed_extremes = remove_extremes(numbers, 2)

        print("List with extremes removed:")
        print(removed_extremes)
        print("Original list:")
        print(numbers)

    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()
