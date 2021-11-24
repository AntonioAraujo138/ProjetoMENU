
list_produto = []
list_cliente = []
list_pedido = []

def produto():
    while True:
        list_produto.append(input('Nome do Produto: '))
        list_produto.append(int(input('Quantidade: ')))
        volta = str(input('Voltar ao Menu [S/N]: '))
        if volta in 'Ss':
            break

def cliente():
    while True:
        list_cliente.append(input('Nome do Cliente: '))
        list_cliente.append(int(input('Telefone: ')))
        volta = str(input('Voltar ao Menu [S/N]: '))
        if volta in 'Ss':
            break

def pedido():
    while True:
        list_pedido.append(float(input('Pedido de: ')))
        list_pedido.append(int(input('Quantidade: ')))
        volta = str(input('Voltar ao Menu [S/N]: '))
        if volta in 'Ss':
            break

def menu():
    print(10*'*', ' M E N U . LOGistica ', 10*'*' )
    print(5*'-', '[1] Cadastrar Produto', 5*'-')
    print(5*'-', '[2] Cadastrar Cliente', 5*'-')
    print(5*'-', '[3] Pedidos ', 5*'-')
    print(5*'-', '[4] Estoque de Produto', 5*'-')
    print(5*'-', '[5] Sair', 5*'-' )


menu()

op = 0
while op != 5: 

#executo oque ele quer fazer
    op = int(input('Digite a opção: '))

    if op == 1:
        produto()
        menu()

    elif op == 2:    
        cliente()
        menu()

    elif op ==3:
        pedido()
        menu()

    elif op == 4:
        print(list_produto)
        while True:
            volta = str(input('Voltar ao Menu [S/N]: '))
            if volta in 'Ss':
                break
        menu()

    elif op == 5:
        print(5*'*','Finalizando..... ',5*'*')
    else:
        print('Opção inválida. Tente Novamente. ')

print('\n Fim do Programa.')


