secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso nao vale, digite apenas uma letra ')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhul, a letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'Ixi, a letra "{letra}" nao existe na palavra secreta. ')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Aeeee, ganhou, a palavra secreta é {secreto_temporario}!')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
        print(f'Voce ainda tem {chances} chances.')