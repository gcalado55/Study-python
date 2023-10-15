import json
import os

def carregarFilmes():
    with open("D:/GitHub/studies-python/AV1/Lista 2/filmes.json", "r") as arquivo:
        filmes = json.load(arquivo)
    return filmes

def salvarFilmes(filmes):
    with open("D:/GitHub/studies-python/AV1/Lista 2/filmes.json", "w") as arquivo:
        json.dump(filmes, arquivo, indent=4)

def exibirFilmes(filmes):
    print("Filmes disponíveis:")
    for filme, horarios in filmes.items():
        print(filme)
        for i, horario in enumerate(horarios, 1):
            print(f"{i}. {horario}")

def fazerReserva(filmes):
    exibirFilmes(filmes)
    filmeEscolhido = input("Escolha um filme: ")

    if filmeEscolhido in filmes:
        horarios = filmes[filmeEscolhido]
        print("Horários disponíveis:")
        for i, horario in enumerate(horarios, 1):
            print(f"{i}. {horario}")
        horario_escolhido = int(input("Escolha um horário (1/2/3): "))
        
        if 1 <= horario_escolhido <= len(horarios):
            qtd_ingressos = int(input("Quantos ingressos deseja comprar? "))
            
            reserva = {
                "filme": filmeEscolhido,
                "horario": horarios[horario_escolhido - 1],
                "qtd_ingressos": qtd_ingressos
            }
            
            if not os.path.exists("D:/GitHub/studies-python/AV1/Lista 2/reservas.json"):
                open("D:/GitHub/studies-python/AV1/Lista 2/reservas.json", "w").close()  
            
            with open("D:/GitHub/studies-python/AV1/Lista 2/reservas.json", "a") as arquivo:
                arquivo.write(json.dumps(reserva) + "\n")
                
            print("Reserva realizada com sucesso!")
        else:
            print("Opção de horário inválida.")
    else:
        print("Filme não encontrado.")

def exibirReservas():
    with open("D:/GitHub/studies-python/AV1/Lista 2/reservas.json", "r") as arquivo:
        for linha in arquivo:
            reserva = json.loads(linha)
            print(f"Filme: {reserva['filme']}, Horário: {reserva['horario']}, Ingressos: {reserva['qtd_ingressos']}")

def main():
    filmes = carregarFilmes()
    while True:
        print("\nOpções:")
        print("1. Exibir filmes disponíveis")
        print("2. Fazer reserva")
        print("3. Exibir reservas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            exibirFilmes(filmes)
        elif escolha == '2':
            fazerReserva(filmes)
        elif escolha == '3':
            exibirReservas()
        elif escolha == '4':
            print("Saindo do programa.")
            salvarFilmes(filmes)
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()