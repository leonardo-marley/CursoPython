"""
nome = 'Leonardo Marley'
idade = 26
altura = 1.75
emaior = idade > 18
peso = 66
imc = peso / (altura ** 2)

print(nome,'você tem', idade,'anos de idade e seu IMC é:', imc)
print(f'{nome} você tem {idade} anos de idade e seu IMC é: {imc:.2f}')
print('{} você tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))
"""

# Exercício teste
import datetime

date = datetime.date.today()
nome = 'Leonardo Marley'
idade = 26
altura = 1.75
peso = 66
ano_atual = date.strftime("%Y")
imc = peso / (altura ** 2)
ano_nascimento = int(ano_atual) - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu no ano de {ano_nascimento}')