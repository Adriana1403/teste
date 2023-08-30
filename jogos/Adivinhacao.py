print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite um número:")

print("Voce digitou: ", chute_str)
chute = int(chute_str)

if numero_secreto == chute:
    print("Acertou miseravi!")
else:
    if chute > numero_secreto:
        print("Você errou! O seu chute foi maior que o número secreto.")
    if chute < numero_secreto:
        print("Você errou! O seu chute foi menor que o númenro secreto")


        print("Fim do jogo")