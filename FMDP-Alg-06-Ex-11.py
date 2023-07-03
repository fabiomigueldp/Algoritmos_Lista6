'''11. Mega-sena. Para ganhar o prêmio da mega-sena, é necessário acertar todos os 6 números
em seu bilhete com os 6 números entre 1 e 60 sorteados pelo organizador da loteria. Escreva
um programa que gere uma seleção aleatória de 6 números para um bilhete de mega-sena.
Certifique-se de que não haja números repetidos entre os sorteados. Exiba os números em
ordem crescente.'''

import random

def gerar_bilhete_mega_sena():
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    return numeros

def main():
    bilhete = gerar_bilhete_mega_sena()

    print("Seu bilhete da Mega-Sena:")
    for numero in bilhete:
        print(numero)


main()
