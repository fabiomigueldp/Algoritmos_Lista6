'''16. Infix para posfix. As expressões matemáticas são frequentemente escritas na forma de infixo,
onde os operadores aparecem entre os operandos sobre os quais atuam. Embora seja uma
forma comum, também é possível expressar expressões matemáticas na forma pós-fixada, em
que o operador aparece depois de ambos os operandos. Por exemplo, a expressão infixa
3 + 4 é escrita como 3 4 + na forma pós-fixada. Pode-se converter uma expressão infixada
em uma forma pós-fixada usando o seguinte algoritmo:
Entrada: lista de tokens infix
Sa ́ıda: lista de tokens postfix
crie uma nova lista vazia, operadores
crie uma nova lista vazia, postfix
para cada token da lista infix fa ̧ca
se token for um nu ́mero inteiro ent ̃ao
Adicione o token ao final de postfix
fim
se token for um operador ent ̃ao
enquanto operadores n ̃ao estiver vazio e o u ́ltimo item em
operadores n ̃ao  ́e um parˆentese aberto e
precedˆencia(token)<precedˆencia(u ́ltimo item em operadores)
fa ̧ca
Remova o u ́ltimo item de operadores e adicione em postfix
fim
Adicione token ao final dos operadores
fim
se token for um parˆentese aberto ent ̃ao
Adicione o token ao final dos operadores
fim
se token for um parˆentese fechado ent ̃ao
enquanto u ́ltimo item nos operadores n ̃ao for um parˆentese
aberto fa ̧ca
Remova o u ́ltimo item dos operadores e adicione-o ao postfix
fim
Remova de operadores o parˆentese aberto
fim
fim
enquanto operadores n ̃ao for uma lista vazia fa ̧ca
Remova o u ́ltimo item dos operadores e adicione-o a postfix
fim
retorna postfix
Use a solução do exercício anterior para tokenizar uma expressão matemática. Em seguida,
use o algoritmo acima para transformar a expressão da forma infixo para a forma pós-fixada.
Seu código que implementa o algoritmo acima deve residir em uma função que recebe uma
lista de tokens que representam uma expressão infixa como seu único parâmetro. Ele deve
retornar uma lista de tokens que representam a expressão pós-fixada equivalente como seu
único resultado. Inclua um programa principal que demonstra sua função infixo para pós-fixada 
lendo uma expressão do usuário na forma infixo e exibindo-a na forma pós-fixada.
A finalidade da conversão da forma infixo para a forma pós-fixada ficará evidente quando você
fizer o próximo exercício. Os exercícios 9 da lista 5 e 14 da lista atual podem ser úteis para
concluir este problema.

Observação: os algoritmos implementados nos exercícios 16 e 17 não realizam nenhuma
verificação de erro. Como resultado, você pode travar seu programa ou receber resultados
incorretos se fornecer dados inválidos. Esses algoritmos podem ser estendidos para
detectar entrada inválida e responder a ela de maneira apropriada. Isto fica como um
exercício de estudo independente para o aluno interessado em aprimorar ainda mais suas
habilidades de programação.'''

def precedencia(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/':
        return 2
    elif operador == '^':
        return 3
    else:
        return -1

def tokenizacao(expressao):
    tokens = []
    token = ""
    for char in expressao:
        if char.isdigit():
            token += char
        elif char in '+-*/^()':
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
    if token:
        tokens.append(token)
    return tokens

def infixo_para_posfixo(tokens):
    operadores = []
    posfixo = []
    for token in tokens:
        if token.isdigit():
            posfixo.append(token)
        elif token in '+-*/^':
            while operadores and operadores[-1] != '(' and precedencia(token) <= precedencia(operadores[-1]):
                posfixo.append(operadores.pop())
            operadores.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                posfixo.append(operadores.pop())
            if operadores and operadores[-1] == '(':
                operadores.pop()
    while operadores:
        posfixo.append(operadores.pop())
    return posfixo

def main():
    expressao = input("Digite uma expressão matemática na forma infixa: ")
    tokens = tokenizacao(expressao)
    posfixo = infixo_para_posfixo(tokens)
    print("Expressão pós-fixada:", ' '.join(posfixo))

main()

