class ConversorMoedas:
    def __init__(self):
        self.taxas = {
            'USD': 1.0,
            'EUR': 0.85,
            'BRL': 5.0,
            'JPY': 110.0,
        }

    def converter(self, valor, moeda_de, moeda_para):
        if moeda_de not in self.taxas or moeda_para not in self.taxas:
            return None
        
        taxa_de = self.taxas[moeda_de]
        taxa_para = self.taxas[moeda_para]

        valor_convertido = valor * (taxa_para / taxa_de)
        return valor_convertido

def main():
    conversor = ConversorMoedas()

    while True:
        print("\nOpções:")
        print("1. Converter moeda")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            moeda_de = input("Digite a moeda de origem (ex: USD): ").upper()
            moeda_para = input("Digite a moeda de destino (ex: EUR): ").upper()
            valor = float(input("Digite o valor a ser convertido: "))
            
            resultado = conversor.converter(valor, moeda_de, moeda_para)
            
            if resultado is not None:
                print(f"{valor} {moeda_de} é igual a {resultado} {moeda_para}")
            else:
                print("Moeda não suportada.")
        elif escolha == '2':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()