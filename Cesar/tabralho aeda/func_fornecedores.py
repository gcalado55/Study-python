import os
import json

def create_func():
    caminho_arquivo = "d:/GitHub/studies-python/Cesar/tabralho aeda/fornecedores.json"
    
    fornecedor = {
        "nome": input("Digite o nome do fornecedor: "),
        "cnpj": input("Digite o CNPJ do fornecedor: "),
        "telefone": input("Digite o telefone do fornecedor: "),
        "produtos": []
    }

    while True:
        produto = input("Digite o nome de um produto fornecido (ou 'sair' para finalizar): ")
        if produto.lower() == 'sair':
            break
        fornecedor["produtos"].append(produto)

    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        dados_existentes = []

    dados_existentes.append(fornecedor)

    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)

    print("\nFornecedor salvo com sucesso!")
    return fornecedor

novo_fornecedor = create_func()

print("\nFornecedor criado:")
print(f"Nome: {novo_fornecedor['nome']}")
print(f"CNPJ: {novo_fornecedor['cnpj']}")
print(f"Telefone: {novo_fornecedor['telefone']}")
print("Produtos fornecidos:")
for produto in novo_fornecedor['produtos']:
    print(f"- {produto}")