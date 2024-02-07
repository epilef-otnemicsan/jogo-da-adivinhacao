import random
numero_secreto = random.randrange(1, 11)
total_tentativas = 0
rodada = 1
pontos = 100
pontos_perdidos = 0

print("-----------------------------------")
print(" Bem vindo ao jogo de Adivinhação! ")
print("-----------------------------------")
print("Escolha abaixo o nível de dificuldade do jogo: ")
print("[ 1 ] Fácil")
print("[ 2 ] Médio")
print("[ 3 ] Difícil")
print("")

nivel = int(input("=> "))
print("")

if nivel == 1:
    total_tentativas = 7
elif nivel == 2:
    total_tentativas = 5
else:
    total_tentativas = 3

while rodada <= total_tentativas:
    if rodada == total_tentativas:
        print(f"Última tentativa!")
    else:
        print(f"Tentativa {rodada} de {total_tentativas}")

    chute = int(input("Digite um número entre 1 e 10: "))
    print("")

    if chute < 1 or chute > 10:
        print("ERRO! Você deve digitar um número entre 1 e 10")
        print("----------------------------------------------")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    print("Você escolheu o número" " [", chute, "]")

    if acertou:
        print(f"Você acertou o número secreto e fez {pontos} pontos")
        print("YOU WIN!")
        break
    else:
        if maior:
            print("Você errou! O número escolhido é maior que o número secreto!")
        elif menor:
            print("Você errou! O número escolhido é menor que o número secreto!")
        if rodada == total_tentativas:
            print("GAME OVER!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    rodada = rodada + 1
    print("")
