"""
Slipt, Join, Enumerate em Pyhton
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # str / iteraiveis
"""

frase = "Python é muito legal, estou gostando muito de aprender, é show de bola!"
lista = frase.split(' ')  # aqui separa por espaco
lista2 = frase.split(',')  # aqui separa por virgula
print(lista, lista2)

# contar palavras
for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase.')

# qual palavra apareceu mais vezes na frase
palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é: "{palavra}" e a contagem de vezes é: ({contagem}x)')

# retirando espaço de uma frase e alterando o inicio da letra para maiuscula
for valor in lista2:
    print(valor.strip().capitalize())

# Join
frase2 = 'Python é muito legal'
lista3 = frase2.split(' ')
frase3 = ','.join(lista3)
print(frase3)

# Enumerate
frase4 = 'Python é muito legal'
lista4 = frase4.split(' ')

for indice, valor in enumerate(lista4):
    print(indice, valor)
