'''6. Lista de divisores. Um divisor de um numero inteiro n é um número inteiro positivo menor
que n, tal que divida n em partes inteiras (divisão exata, sem resto). Escreva uma função
Python que calcula todos os divisores de um número inteiro positivo. A função deve retornar
uma lista contendo todos os divisores. Escreva uma função main para demonstrar o
funcionamento da sua solução, a função main deve ler um número do usuário e imprimir todos
os seus divisores.'''

def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def main():
    num = int(input("Enter a positive integer: "))
    divisors = find_divisors(num)
    print("Divisors of", num, ":")
    for divisor in divisors:
        print(divisor)

main()
