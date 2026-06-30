frutas = ["uva", "maça", "pitaya", "pera", "banana"]
print(frutas) #['uva', 'maça', 'pitaya', 'pera', 'banana']

print('Qual a fruta que você deseja adicionar na lista: ?')

nova_fruta = input('A fruta escolhida foi: ')
frutas.append(nova_fruta)
print(f'Essas são as nossas frutas: {frutas}')


# Eu posso remover e adicionar elementos
# variavel + atributo devo usar o ponto "frutas.append(nova_fruta)"
# para adicionar a fruta na lista