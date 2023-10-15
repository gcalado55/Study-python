class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

def main():
    caixa = CaixaEletronico()

    while True:
        print("\nOpções:")
        print("1. Consultar saldo")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            saldo = caixa.consultar_saldo()
            print("Saldo atual: R$", saldo)
        elif escolha == '2':
            valor_deposito = float(input("Digite o valor a ser depositado: R$"))
            if caixa.depositar(valor_deposito):
                print("Depósito realizado com sucesso.")
            else:
                print("Valor inválido. O valor do depósito deve ser maior que zero.")
        elif escolha == '3':
            valor_saque = float(input("Digite o valor a ser sacado: R$"))
            if caixa.sacar(valor_saque):
                print("Saque realizado com sucesso.")
            else:
                print("Saque não realizado. Saldo insuficiente ou valor inválido.")
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()