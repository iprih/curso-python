"""
CPF = 168.995.350-09
-------------------------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
---------------------------------------------------------------------
# meu teste abaixo eu retirei os pontos do cpf e deixei apenas os 9 primeiros digitos, porém vou seguir a resolução do professor!
CPF = '168.995.350-09'
CPF2 = CPF.split('.')
print(CPF2)
CPF3 = ''.join(CPF2)
print(CPF3)
CPF4 = CPF3.split('-')
CPF5 = CPF4[0]
print(CPF5)
"""

cpf = '16899535009'
novo_cpf = cpf[:-2]  # esse comando retira os dois ultimos digitos
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
# Evita sequencias
sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
if cpf == novo_cpf and not sequencia:
    print('Valido')
else:
    print('Invalido')
print(novo_cpf)

# Com input
while True:
    cpf = input('Digite um cpf: ')

    novo_cpf = cpf[:-2]  # esse comando retira os dois ultimos digitos
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    if cpf == novo_cpf:
        print('Valido')
    else:
        print('Invalido')
    print(novo_cpf)




