'''
>>Projeto açaíteria:
'''



# Ufa, quebrei a maldição
# print('Olá, Mundo!')


print('-' * 48 + '\n')
print('Bem-vindo ao Sistema de vendas - Açaíteria!\n')
print('1 - Cadastrar produto')
print('2 - Lista de produtos')
print('3 - Realizar venda')
print('4 - Açaí')
print('5 - Toppings')
print('6 - Localização')
print('7 - Contato')
print('8 - Redes Sociais')
print('9 - Feedback')
print('0 - Sair do Sistema')
print('\n--------------------------------------\n')


opcao__definida = int(input('Digite a opção desejada: '))

if opcao__definida == 1:
    print('Cadrastanto produto...')

elif opcao__definida == 2:
    print('Listando produto...')

elif opcao__definida == 3:
    print('Realizar venda...')

elif opcao__definida == 4:
    print('Preparando o seu Açaí...')

elif opcao__definida == 5:
    print('Acrescentando os Toppings...')

elif opcao__definida == 6:
    print('Visualizando a sua localização..')

elif opcao__definida == 7:
    print('Entrando em contato...')

elif opcao__definida == 8:
    print('Aproveite esse tempo de entrega e nos siga nas redes sociais!...')

elif opcao__definida == 9:
    print('Pronto! Gostariamos que você enviasse o seu feedback')

else:
    print('Humm, Algo deu errado. Tente Novamente!')
