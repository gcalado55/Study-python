import csv

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    with open("D:/GitHub/studies-python/AV1/Lista 2/agenda.csv", mode="a", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, telefone, email])
    
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    with open("D:/GitHub/studies-python/AV1/Lista 2/agenda.csv", mode="r") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print(f"Nome: {linha[0]}\nTelefone: {linha[1]}\nE-mail: {linha[2]}\n")

def buscar_contato():
    nome_busca = input("Nome a ser buscado: ")
    
    with open("D:/GitHub/studies-python/AV1/Lista 2/agenda.csv", mode="r") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        encontrado = False
        for linha in leitor:
            if linha[0] == nome_busca:
                print(f"Nome: {linha[0]}\nTelefone: {linha[1]}\nE-mail: {linha[2]}\n")
                encontrado = True
                break
        
        if not encontrado:
            print(f"Contato com o nome {nome_busca} não encontrado.")

def remover_contato():
    nome_remover = input("Nome a ser removido: ")
    
    with open("D:/GitHub/studies-python/AV1/Lista 2/agenda.csv", mode="r") as arquivo_csv:
        linhas = list(csv.reader(arquivo_csv))
    
    encontrado = False
    with open("D:/GitHub/studies-python/AV1/Lista 2/agenda.csv", mode="w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for linha in linhas:
            if linha[0] == nome_remover:
                print(f"Contato {linha[0]} removido com sucesso!")
                encontrado = True
            else:
                escritor.writerow(linha)
    
    if not encontrado:
        print(f"Contato com o nome {nome_remover} não encontrado na agenda.")

def main():
    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            remover_contato()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
