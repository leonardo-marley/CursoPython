"""
Operadores relacionais
(==) (>) (>=) (<) (<=)  (!=)
"""
nome = input('Qual o seu nome? \n')
idade = input('Qual sua idade? \n')

if 18 <= int(idade) <= 30:
    print(f'{nome}, impréstimo solicitado com sucesso.')
else:
    print(f'{nome}, você precisa do apoio de um responsável legal.')

"""
Operadores lógicos
(and) / (or) / (not) / (in) / (not in)
"""

a = ''
b = 0

if not b:
    print('Preencha um valor para B')  # O not na frente sinaliza se a variável está vazia ou não
