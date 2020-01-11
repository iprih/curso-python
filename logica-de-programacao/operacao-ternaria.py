"""
logged_user = False

if logged_user == True:
    msg = 'Usuario logado'
else:
    msg = 'Usuario precisa logar'

print(msg)
"""
# usando o mesmo conceito com ternario
logged_user = False
msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'
print(msg)

# outro exemplo
idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Voce precisa digitar apenas números')
else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    msg2 = 'Pode acessar, é de maior' if maior_de_idade else 'Nao pode acessar pois é de menor.'
    print(msg2)