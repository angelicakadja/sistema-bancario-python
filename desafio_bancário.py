menu = """
============================================================
\n     SEJA MUITO(A) BEM-VINDO(A) AO NOSSO BANCO VIRTUAL!
\n============================================================
\n✋ Como podemos lhe ajudar hoje?
Por gentileza escolha um número:
\n----------------------
╔═════════════════════╗
          MENU         
-----------------------
  [0] - 📄 Extrato    
  [1] - 💸 Sacar      
  [2] - 💰 Depositar  
  [3] - 🚪 Sair       
╚═════════════════════╝
=> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0": #extrato
        print ("\n================================================")
        print ("Extrato Conta Corrente")
        print ("------------------------------------------------")
        print ("Lançamentos:")
        print ("\nNão foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print ("\n================================================")
        
    elif opcao == "1": #sacar
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_diario

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("💢 Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print(f"\n💢 Operação falhou! O valor do saque excede o limite de R$ {limite_diario:.2f} por transação.")

        elif excedeu_saques:
            print(f"Você já atingiu o limite de {LIMITE_SAQUES} saques por dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print ("\n❌ Operação falhou! O valor informado é inválido.")
    
    elif opcao == "2": #depositar
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            confirm = int(input(f"Por gentileza, confirma o valor de R$ {valor} para depósito?\n [1] - SIM\n [2] - NÃO\n"))
            if confirm == 1:
                extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n✔️  Depósito efetuado com sucesso! Seu saldo atual é de R$ {saldo:.2f}.")
        
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "3": #sair
        print("Obrigado por usar nossos serviços. 🤝")
        print("Até breve! 👋\n")
        break
    
    else:
        print ("❌ Operação inválida, por favor selecione novamente a operação desejada.")