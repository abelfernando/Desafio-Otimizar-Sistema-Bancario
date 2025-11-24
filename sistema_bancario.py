def deposito(saldo, valor, extrato, /):
    """Realiza um depósito na conta bancária.
    Parâmetros apenas por posição: (saldo, valor, extrato)"""

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato
    

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza um saque na conta bancária.
    Parâmetros apenas por nome: (saldo, valor, extrato, limite, numero_saques, limite_saques)"""

    if valor > limite + saldo:
        print("Operação falhou! Você não tem saldo suficiente e o valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato da conta bancária.
    Parâmetros por posição ou por nome: (saldo, extrato)"""

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("==========================================")


def menu():
    """Exibe o menu de opções do sistema bancário."""
    menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """
    return input(menu)


def main():
    """Função principal do sistema bancário."""
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
    
        opcao = menu()
    
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
    
            saldo, extrato = deposito(saldo, valor, extrato)
    
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
    
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
    
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()