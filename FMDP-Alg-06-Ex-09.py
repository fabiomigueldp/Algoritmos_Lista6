'''9. Abaixo e acima da média. Escreva um programa que leia números do usuário até que uma
linha em branco seja inserida. Seu programa deve exibir a média de todos os valores inseridos
pelo usuário. Em seguida, o programa deve exibir todos os valores abaixo da média, seguidos
por todos os valores médios (se houver), seguidos por todos os valores acima da média. Uma
mensagem apropriada deve ser exibida antes de cada lista de valores.'''

def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media


def classificar_numeros(numeros, media):
    abaixo_da_media = []
    igual_a_media = []
    acima_da_media = []

    for numero in numeros:
        if numero < media:
            abaixo_da_media.append(numero)
        elif numero > media:
            acima_da_media.append(numero)
        else:
            igual_a_media.append(numero)

    return abaixo_da_media, igual_a_media, acima_da_media


def main():
    numeros = []
    
    while True:
        valor = input("Digite um número (linha em branco para parar): ")
        if valor == "":
            break
        numeros.append(float(valor))

    if len(numeros) == 0:
        print("Nenhum número digitado.")
        return

    media = calcular_media(numeros)
    abaixo_da_media, igual_a_media, acima_da_media = classificar_numeros(numeros, media)

    print("Números abaixo da média:")
    for numero in abaixo_da_media:
        print(numero)

    print("\nNúmeros iguais à média:")
    for numero in igual_a_media:
        print(numero)

    print("\nNúmeros acima da média:")
    for numero in acima_da_media:
        print(numero)

main()
