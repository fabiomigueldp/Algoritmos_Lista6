'''8. Somente palavras. Neste exercício você deve criar uma função em Python que recebe um
texto em uma string e retorna uma lista somente com as palavras, sem espaços ou símbolos
de pontuação. Por exemplo, se a string for: “Beleza! Este é um ótimo exemplo, você
não acha?”, sua função deveria retornar a seguinte lista: [ “Beleza", “Este", “é",
“um", “ótimo", "exemplo", “você", “não", “acha”]. Escreva uma função main
que demonstre o funcionamento da sua solução.'''

import string

def extract_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()
    
    return words


def main():
    text = "Beleza! Este é um ótimo exemplo, você não acha?"
    words = extract_words(text)
    print(words)

main()
