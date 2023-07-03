'''13. Contagem de elementos. A biblioteca padrão de funções do Python possui um método
chamado count, que determina quantas vezes um determinado valor ocorre em uma lista.
Neste exercício você deve criar uma nova função chamada countRange que deve determinar
e retornar a quantidade de elementos em uma lista que são maiores ou iguais a um valor
mínimo e menores que um valor máximo. Sua função deve receber três parâmetros: a lista (de
números), o valor mínimo e o valor máximo. Ela deve retornar um valor inteiro maior ou igual a
zero. Escreva uma função main demonstrando o funcionamento de sua função.'''

def countRange(lista, minimo, maximo):
    count = 0
    for elemento in lista:
        if minimo <= elemento < maximo:
            count += 1
    return count

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    minimo = 3
    maximo = 7
    quantidade = countRange(lista, minimo, maximo)
    print(f"A quantidade de elementos na lista entre {minimo} e {maximo} é: {quantidade}")

main()
