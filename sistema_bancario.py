# Dio_lab_Sistema_Banc-rio_python
# Desafio Dio de criar um sistema bancario 


import datetime

# Variáveis do sistema
saldo = 0.0
limite_saque = 500.00
saques_realizados = 0
limite_saques_diarios = 3
extrato = []

def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: {formatar_valor(valor)}")
        print("Depósito realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

def sacar(valor):
    global saldo, saques_realizados
    if saques_realizados >= limite_saques_diarios:
        print("Limite diário de saques atingido.")
    elif valor > limite_saque:
        print(f"O limite por saque é de {formatar_valor(limite_saque)}.")
    elif valor > saldo:
        print("Saldo insuficiente para saque.")
    elif valor <= 0:
        print("Valor de saque inválido.")
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f"Saque:    {formatar_valor(valor)}")
        print("Saque realizado com sucesso.")

def ver_extrato():
    print("\n======== EXTRATO ========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: {formatar_valor(saldo)}")
    print("==========================\n")

def menu():
    while True:
        print("Escolha uma operação:")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[0] Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            try:
                valor = float(input("Informe o valor para depósito: R$ "))
                depositar(valor)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif opcao == '2':
            try:
                valor = float(input("Informe o valor para saque: R$ "))
                sacar(valor)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif opcao == '3':
            ver_extrato()
        elif opcao == '0':
            print("Encerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar sistema
menu()
