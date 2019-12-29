"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# acessa o caracter desejado
texto = 'Valor'
print(texto[1])

lista = [1, 2, 3, 4, 'Priscila']

# pega o ultimo valor do objeto
print(lista[4])
# pega o ultimo valor do objeto
print(lista[-1])
# pula de dois em dois
print(lista[::2])

# append insere na lista
l1 = [1, 2, 3]
l1.append('b')
print(l1)

# ou com insert colocando o parametro indice e depois o valor desejado
l1.insert(0, 'banana')
print(l1)

# pop remove o elemento da lista
l2 = [4, 5, 6, 'banana']
print(l2)
l2.pop()
print(l2)

# del escolhendo o indice, no exemplo abaixo esta escluindo do 4 ao 5
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l3)
del(l3[3:5])
print(l3)

print(max(l3))
print(min(l3))

# range
l4 = list(range(1, 21))
print(l4)
# multiplos de 8 de 0 a 100
l5 = list(range(0, 100, 8))
print(l5)

# utilizando o for
l6 = list(range(1, 10))
print(l6)
soma = 0
for valor in l6:
    soma = soma + valor

print(f'{soma} + {valor} = {soma}')

# adivinhando a palavra

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
        print(f'Perdeu a palavra secreta está assim {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
        print(f'voce ainda tem {chances} chances.')