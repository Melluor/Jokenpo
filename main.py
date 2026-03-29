import random

opcoes = ['pedra', 'papel', 'tesoura']

def jogadas():
    jogador = input("Escolha sua mão: ").strip().lower()
    computador = random.choice(opcoes)
    if jogador not in opcoes:
        print("Mão inválida!")
    if jogador == computador:
        print(f"Empate! Ambos escolheram {computador}!")
        return 'Empate'
    elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
        print(f"Você venceu o duelo! Você escolheu {jogador} e o Oponente escolheu {computador}!")
        return 'Jogador'
    else:
        print(f"Você perdeu o duelo! O oponente escolheu {computador} e você escolheu {jogador}!")
        return 'Computador'

def melhor_de_3():
    x = y = 0
    while x < 2 and y < 2:
        resultado = jogadas()
        if resultado == 'Empate':
            print('Empate!\n')
        if resultado == 'Jogador':
            x += 1
            print(f'Ponto para você! {x} - {y}\n')
        else:
            y += 1
            print(f'Ponto para o Pc! {x} - {y}\n')
    if x == 2:
        print(f'Você venceu o jogo! PC: {y} pontos- Jogador: {x} pontos\n')
    else:
        print(f'Pc venceu o jogo! PC: {y} pontos - Jogador: {x} pontos\n')

def melhor_de_5():
    x = y = 0
    while x < 3 and y < 3:
        resultado = jogadas()
        if resultado == 'Empate':
            print('Empate!\n')
        if resultado == 'Jogador':
            x += 1
            print(f'Ponto para você! {x} - {y}\n')
        else:
            y += 1
            print(f'Ponto para o oponente! {x} - {y}\n')
    if x == 3:
        print(f"Você venceu o duelo! PC: {y} pontos - Jogador: {x} pontos\n")
    else:
        print(f"O oponente venceu o duelo! PC: {y} pontos - Jogador: {x} pontos\n")

escolha = int(input("""
1. Jogo Simples
2. Melhor de 3
3. Melhor de 5
4. Regras
5. Sair
: """))

match escolha:
    case 1:
        jogadas()
    case 2:
        melhor_de_3()
    case 3:
        melhor_de_5()
    case 4:
        print('Cada jogador escolhe uma mão entre Pedra, Papel e Tesoura.\n')
        print('Jogadores com a mesma mão resulta em empate.\n')
        print('Pedra quebra Tesoura; Papel embrulha Pedra; Tesoura corta Papel.\n')
    case 5:
        print('Thank You! Bye Bye')
