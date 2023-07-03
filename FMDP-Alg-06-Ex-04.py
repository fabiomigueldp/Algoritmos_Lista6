'''4. Evitando duplicatas. Crie um programa Python que leia palavras do teclado até que o
usuário forneça uma palavra vazia (somente a tecla enter). Depois disso, seu programa deve
mostrar somente uma vez cada palavra digitada pelo usuário. Ou seja, se o usuário forneceu
mais de uma vez a mesma palavra, ela só poderá ser exibida uma vez. As palavras devem ser
exibidas na mesma ordem em que foram digitadas. Por exemplo, se o usuário digitar:
Primeira
Segunda
Primeira
Terceira
Segunda
Então seu programa deve exibir:
Primeira
Segunda
Terceira'''

def remove_duplicates(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def main():
    words = []
    while True:
        word = input("Enter a word (press Enter to stop): ")
        if word == "":
            break
        words.append(word)

    unique_words = remove_duplicates(words)

    for word in unique_words:
        print(word)

main()
