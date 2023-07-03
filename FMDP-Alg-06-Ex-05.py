'''5. Negativos, zeros e positivos. Escreva um programa Python que leia números inteiros até
que uma linha em branco seja fornecida pelo usuário (se ele digitar somente enter). Depois
que todos os inteiros tiverem sido lidos, seu programa deve mostrar todos os números
negativos, seguidos por todos os zeros e depois todos os números positivos. Dentro de cada
grupo os números devem ser exibidos na ordem em que foram fornecidos pelo usuário. Por
exemplo, se o usuário forneceu os valores 3, -4, 1, 0, -1, 0 e -2, então seu programa deve
exibir os valores -4, -1, -2, 0, 0, 3 e 1, cada um em uma linha.'''

def main():
    negatives = []
    zeros = []
    positives = []

    while True:
        num_input = input("Enter an integer (press Enter to stop): ")
        if num_input == "":
            break

        num = int(num_input)
        if num < 0:
            negatives.append(num)
        elif num == 0:
            zeros.append(num)
        else:
            positives.append(num)

    for num in negatives:
        print(num)
    for num in zeros:
        print(num)
    for num in positives:
        print(num)

main()
