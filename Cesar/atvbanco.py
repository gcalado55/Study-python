def banco():
  print("\nSolicitação de emprestimo:")
  sair = 'n'
  while sair != 's':
    valor_casa = float(input("\nDigite o valor da casa desejada: "))
    salario = float(input("Digite o salario do comprador: "))
    prazo = float(input("Digite o prazo de pagamento(em anos): "))
    prestacao_mensal = float(valor_casa/(12 * prazo))
    print("\nPrestação mensal: R$", prestacao_mensal)

    if prestacao_mensal >= (0.3 * salario):
      print("EMPRESTIMO NEGADO, SEU LISO!!!")
    else:
      print("EMPRESTIMO APROVADO!!!")
    
    sair = input("Caso queira sair do progama digite 's':")

def main():
  banco()

if __name__ == '__main__':
  main()
  






  