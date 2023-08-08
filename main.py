menu = """
====================
[d] = deposito
[s] = saque
[e] = extrato
[q] = sair
====================
"""

saldo = 0
limite = 500
numeroSaques = 0
LIMITE_SAQUES = 3
extratoDep= ""
extratoSaq= ""
print(menu)
while True:
    opcao = input("Escolha uma opção: ")
    if opcao == 'q':
        print("Saindo do programa...")
        break
    elif opcao == 'd':
        print("Opção escolhida: Depósito")
        valor = float(input("Digite o valor do depósito: "))
        if (valor > 0):
            saldo += valor
            extratoDep += str(valor) + "- "
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido!")
    elif opcao == 's':
        print("Opção escolhida: Saque")
        valor = float(input("Digite o valor do saque: "))
        if 0 < valor <= saldo and numeroSaques < LIMITE_SAQUES and valor <= 500:
            saldo -= valor
            numeroSaques += 1
            extratoSaq += str(valor) + "- "
            print("Saque realizado com sucesso!")
        elif valor > saldo:
            print("valor maior que o saldo!")
        elif numeroSaques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
        elif valor > limite:
            print("Valor maior que o limite!")
        else:
            print("Valor inválido!")
    elif opcao == 'e':
        print("Opção escolhida: Extrato")
        print("Extrato de depósitos: ", extratoDep)
        print("Extrato de saques: ", extratoSaq)
        print("Saldo: R$ ", saldo)
    else:
        print("Opção inválida!")
    print()
    print(menu)
