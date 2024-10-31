import os
import json

def create_forn():
    caminho_arquivo = "d:/GitHub/studies-python/Cesar/tabralho aeda/fornecedores.json"
    
    dados_existentes = []
    
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)

    while True:
        cnpj = input("Digite o CNPJ do fornecedor: ")
        if any(fornecedor["cnpj"] == cnpj for fornecedor in dados_existentes):
            print("Já existe um fornecedor com esse CNPJ. Digite um CNPJ diferente.")
        else:
            break

    while True:
        telefone = input("Digite o telefone do fornecedor: ")
        if any(fornecedor["telefone"] == telefone for fornecedor in dados_existentes):
            print("Já existe um fornecedor com esse telefone. Digite um telefone diferente.")
        else:
            break

    fornecedor = {
        "nome": input("Digite o nome do fornecedor: "),
        "cnpj": cnpj,
        "telefone": telefone,
        "desconto": input("Digite o desconto do fornecedor: "),
        "produtos": []
    }

    while True:
        produto = input("Digite o nome de um produto fornecido (ou 'sair' para finalizar): ")
        if produto.lower() == 'sair':
            break
        fornecedor["produtos"].append(produto)

    dados_existentes.append(fornecedor)

    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)

    print("\nFornecedor salvo com sucesso:")
    print(f"Nome: {fornecedor['nome']}")
    print(f"CNPJ: {fornecedor['cnpj']}")
    print(f"Telefone: {fornecedor['telefone']}")
    print(f"Desconto: {fornecedor['desconto']}")
    print("\nProdutos fornecidos:")
    for produto in fornecedor['produtos']:
        print(f"- {produto}")

    return fornecedor

def update_forn():
    caminho_arquivo = "d:/GitHub/studies-python/Cesar/tabralho aeda/fornecedores.json"
    
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        print("Nenhum fornecedor encontrado.")
        return

    while True:
        cnpj_fornecedor = input("Digite o CNPJ do fornecedor que deseja atualizar (ou 'sair' para cancelar): ")
        if cnpj_fornecedor.lower() == 'sair':
            print("Operação cancelada.")
            return

        fornecedor_encontrado = False
        for fornecedor in dados_existentes:
            if fornecedor["cnpj"] == cnpj_fornecedor:
                fornecedor_encontrado = True
                print("\nFornecedor encontrado. Deixe em branco para manter o valor atual.")
                
                fornecedor["nome"] = input(f"Nome [{fornecedor['nome']}]: ") or fornecedor["nome"]
                
                novo_cnpj = input(f"CNPJ [{fornecedor['cnpj']}]: ") or fornecedor["cnpj"]
                fornecedor["cnpj"] = novo_cnpj
                
                fornecedor["telefone"] = input(f"Telefone [{fornecedor['telefone']}]: ") or fornecedor["telefone"]
                
                fornecedor["desconto"] = input(f"Desconto [{fornecedor['desconto']}]: ") or fornecedor["desconto"]
                
                print("Produtos fornecidos atualmente:")
                for produto in fornecedor["produtos"]:
                    print(f"- {produto}")

                while True:
                    novo_produto = input("Digite um novo produto (ou 'sair' para finalizar a adição): ")
                    if novo_produto.lower() == 'sair':
                        break
                    fornecedor["produtos"].append(novo_produto)

                with open(caminho_arquivo, "w") as arquivo:
                    json.dump(dados_existentes, arquivo, indent=4)

                print("\nFornecedor atualizado com sucesso!")
                print(f"Nome: {fornecedor['nome']}")
                print(f"CNPJ: {fornecedor['cnpj']}")
                print(f"Telefone: {fornecedor['telefone']}")
                print(f"Desconto: {fornecedor['desconto']}")
                print("\nProdutos fornecidos:")
                for produto in fornecedor['produtos']:
                    print(f"- {produto}")

                return fornecedor
        
        if not fornecedor_encontrado:
            print("Fornecedor com CNPJ especificado não encontrado. Tente novamente.")
