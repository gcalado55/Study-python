def create_func():
  fornecedor ={
    "nome": input("Digite o nome do fornecedor: "),
    "cnpj": input("Digite o cnpj do fornecedor: "),
    "telefone": input("Digite o telefone do fornecedor: "),
    "produtos": []
  }

  while True:
    produto = input("Digite o nome de um produto fornecido(ou 'sair' para finalizar): ")