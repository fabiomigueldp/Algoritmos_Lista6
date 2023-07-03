'''17. Avaliação de expressão pós-fixada. Avaliar uma expressão pós-fixada é mais fácil do que
avaliar uma expressão infixa porque ela não contém nenhum colchete e não há regras de
precedência de operador a serem consideradas. Uma expressão pós-fixada pode ser avaliada
usando o seguinte algoritmo:
Crie uma nova lista vazia, valores
para cada token da express ̃ao postfix fa ̧ca
se token for um nu ́mero ent ̃ao
Converta-o para um inteiro e adicione-o ao final de valores
sen ̃ao
Remova um item do final dos valores e chame-o de direita
Remova um item do final dos valores e chame-o de esquerda
Aplique o operador aos itens esquerda e direita
Anexe o resultado ao final de valores
fim
fim
retorna o primeiro item de valores como o valor da express ̃ao
Escreva um programa que leia uma expressão matemática em forma de infixo do usuário, a
avalie e exiba seu valor. Usa suas soluções dos exercícios 15 e 16 junto com o algoritmo
mostrado acima para resolver este problema.'''

def avaliar(expressao):
    valores = []
    operadores = ['+', '-', '*', '/']  # Operadores suportados

    for token in expressao:
        if token.isdigit():
            valores.append(int(token))
        elif token in operadores:
            direita = valores.pop()
            esquerda = valores.pop()

            if token == '+':
                resultado = esquerda + direita
            elif token == '-':
                resultado = esquerda - direita
            elif token == '*':
                resultado = esquerda * direita
            elif token == '/':
                resultado = esquerda / direita

            valores.append(resultado)

    return valores[0]

expressao = input("Digite uma expressão matemática na forma pós-fixada: ").split()
resultado = avaliar(expressao)
print("O resultado da expressão é:", resultado)
