'''7. Números perfeitos. Um número inteiro positivo n é chamado de número perfeito se a soma
de todos os divisores de n é igual a n. Por exemplo, 28 é um número perfeito porque seus
divisores são 1, 2, 4, 7 e 14; e 1+2+4+7+14=28. Escreva uma função para verificar se um
número é perfeito. A função deve receber somente um número inteiro positivo e retornar True
se ele for perfeito ou False caso contrário. Escreva uma função main para identificar e imprimir
todos os números perfeitos de 1 a 10.000. Obs.: você pode usar o código do exercício anterior
para lhe ajudar nesta tarefa.'''

def is_perfect_number(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        return True
    else:
        return False


def main():
    print("Perfect numbers from 1 to 10,000:")
    for num in range(1, 10001):
        if is_perfect_number(num):
            print(num)

main()
