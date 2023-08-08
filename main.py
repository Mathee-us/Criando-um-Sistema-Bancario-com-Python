def menu():
    menu = """
    ====================
    [d] = deposito
    [s] = saque
    [e] = extrato
    [nc] = criar conta
    [lc] = listar contas
    [nu] = novo usuário
    [q] = sair
    ====================
    """
    return menu

def saque(*,saldo, extratoSaq, valor, limite, numeroSaques, LIMITE_SAQUES):
    if 0 < valor <= saldo and numeroSaques < LIMITE_SAQUES and valor <= 500:
        saldo -= valor
        numeroSaques += 1
        extratoSaq += str(valor) + " "
        print("Saque realizado com sucesso!")
        return saldo, extratoSaq, numeroSaques
    elif valor > saldo:
        print("valor maior que o saldo!")
    elif numeroSaques >= LIMITE_SAQUES:
        print("Limite de saques atingido!")
    elif valor > limite:
        print("Valor maior que o limite!")
    else:
        print("Valor inválido!")

def deposito(saldo, extratoDep, valor,/):
    if (valor > 0):
        saldo += valor
        extratoDep += str(valor) + " "
        print("Depósito realizado com sucesso!")
        return saldo, extratoDep
    else:
        print("Valor inválido!")

def extrato(saldo,/, *, extratoDep, extratoSaq ):
    print("Extrato de depósitos: ", extratoDep)
    print("Extrato de saques: ", extratoSaq)
    print("Saldo: R$ ", saldo)

def criar_usuario(usuarios):

    cpf = input("Digite seu cpf: ")
    if cpf in usuarios:
        print("CPF já cadastrado!")
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        endereco = input("Digite seu endereço: ")
        print("Usuário cadastrado com sucesso!")
        usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})


def criar_conta(agencia,usuarios, contas,numero_conta):
    cpf = input("Digite seu cpf: ")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            contas.append({"agencia":agencia,"numero_conta":numero_conta,"usuario":usuarios })
            print("Conta cadastrada com sucesso!")
            return
    print("CPF não cadastrado!")

def listar_contas(contas):
    for conta in contas:
        print(f"Agencia: {conta['agencia']}\n Conta: {conta['numero_conta']} \n")
        for dado in conta['usuario']:
            print(f"Nome: {dado['nome']}\n CPF: {dado['cpf']}\n Data de nascimento: {dado['data_nascimento']}\n Endereço: {dado['endereco']}")

def main():
    saldo = 0
    limite = 500
    numeroSaques = 0
    LIMITE_SAQUES = 3
    extratoDep= ""
    extratoSaq= ""
    usuarios = []
    contas = []
    AGENCIA = 1
    while True:
        print(menu())
        opcao = input("Escolha uma opção: ").lower()
        if opcao == 'q':
            print("Saindo do programa...")
            break
        elif opcao == 'd':
            print("Opção escolhida: Depósito")
            valor = float(input("Digite o valor do depósito: "))
            saldo, extratoDep = deposito(saldo, extratoDep, valor)


        elif opcao == 's':
            print("Opção escolhida: Saque")
            valor = float(input("Digite o valor do saque: "))
            saldo,extratoSaq,numeroSaques = saque( saldo=saldo, extratoSaq=extratoSaq, valor=valor, limite=limite, numeroSaques=numeroSaques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == 'e':
            print("Opção escolhida: Extrato")
            extrato(saldo, extratoDep=extratoDep, extratoSaq=extratoSaq)
        elif opcao == 'nc':
            print("Opção escolhida: Criar conta")
            numero_conta= len(contas)+1
            criar_conta(AGENCIA, usuarios, contas,numero_conta)
        elif opcao == 'lc':
            print("Opção escolhida: Listar contas")
            listar_contas(contas)
        elif opcao == 'nu':
            print("Opção escolhida: Novo usuário")
            criar_usuario(usuarios)
        else:
            print("Opção inválida!")
        print()
        print(menu)

main()
