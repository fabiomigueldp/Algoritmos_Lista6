'''12. A lista está ordenada? Escreva uma função que determina se uma lista de valores está ou
não em ordem de classificação (crescente ou decrescente). A função deve receber a lista
como parâmetro e retornar True se a lista já estiver classificada. Caso contrário, ele deve
retornar False. Escreva um programa principal que leia uma lista de números do usuário e use
sua função para relatar se a lista é classificada.

Observação: certifique-se de considerar estas questões ao concluir este exercício:
Uma lista vazia está em ordem? E uma lista contendo somente um elemento?'''

def lista_ordenada(valores):
    if len(valores) <= 1:
        return True
    
    if valores == sorted(valores) or valores == sorted(valores, reverse=True):
        return True
    else:
        return False

def main():
    numeros = []
    entrada = input("Digite os números da lista (separados por espaço): ")
    numeros = entrada.split()

    # Converte os elementos da lista para inteiros
    numeros = [int(num) for num in numeros]

    if lista_ordenada(numeros):
        print("A lista está em ordem.")
    else:
        print("A lista não está em ordem.")

main()
