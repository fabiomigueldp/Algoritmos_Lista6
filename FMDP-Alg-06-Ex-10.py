'''10. Formatando uma lista. Quando escrevemos uma lista em português, geralmente separamos
os itens por vírgula e colocamos a conjunção “e" entre os dois últimos itens, a não ser que a
lista só tenha um item. Considere as listas abaixo:
maçãs
maçãs e laranjas
maçãs, laranjas e bananas
maçãs, laranjas, bananas e limões
Escreva uma função que receba como parâmetro uma lista de strings e retorne uma única
string contendo todos os itens da lista formatados conforme mostrado acima. Apesar dos
exemplos acima terem no máximo 4 itens, sua função deve se comportar corretamente para
listas de qualquer tamanho. Escreva uma função main demonstrando o funcionamento de sua
função.'''

def formatar_lista(lista):
    tamanho = len(lista)

    if tamanho == 0:
        return ""

    if tamanho == 1:
        return lista[0]

    if tamanho == 2:
        return f"{lista[0]} e {lista[1]}"

    lista_formatada = ", ".join(lista[:-1])
    lista_formatada += f" e {lista[-1]}"

    return lista_formatada


def main():
    lista = []

    while True:
        item = input("Digite um item da lista (linha em branco para parar): ")
        if item == "":
            break
        lista.append(item)

    lista_formatada = formatar_lista(lista)

    print("Lista formatada:")
    print(lista_formatada)



main()
