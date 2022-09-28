usuario = input('Nome de usuário: \n')
senha = input('Senha do usuário: \n')

user_bd = 'leozin'
senha_bd = '123456'

if usuario == user_bd and senha == senha_bd :
    print('Usuário logado.')
else :
    print('Login ou senha incorretos.')
