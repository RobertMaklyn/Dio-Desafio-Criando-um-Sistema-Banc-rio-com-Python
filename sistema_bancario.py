menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('erro! o valor informado é inválido')

    elif opcao == 2:
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        execedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Erro! saldo insuficiente')

        elif excedeu_limite:
            print('Erro! o valor de saque excedeu o limite')

        elif execedeu_saque:
            print('Erro! numero de saque excedidos')

        elif valor > 0:
            saldo -= valor
            extrato += f'saque R$: {valor:.2f}\n'
            numero_saque += 1

        else:
            print('Erro! o valor informado é invalido')

    elif opcao == 3:
        print('\n ========== EXTRATO ==========')
        print('Nao foram realizado movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$: {saldo:.2f}')
        print('================================')

    elif opcao == 4:
        break

    else:
        print('Erro! operação invalida selecione novamente a opção desejada')