import json
import os

def carregar_tarefas():
    try:
        with open("D:/GitHub/studies-python/AV1/Lista 2/tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        tarefas = []
    return tarefas

def salvar_tarefas(tarefas):
    with open("D:/GitHub/studies-python/AV1/Lista 2/tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

def adicionar_tarefa(tarefas, descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas.")
    else:
        for indice, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{indice}. [{status}] {tarefa['descricao']}")

def marcar_tarefa_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice - 1]["concluida"] = True
        salvar_tarefas(tarefas)
    else:
        print("Índice inválido.")

def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        del tarefas[indice - 1]
        salvar_tarefas(tarefas)
    else:
        print("Índice inválido.")

def main():
    tarefas = carregar_tarefas()

    while True:
        print("\nOpções:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
            print("Tarefa adicionada com sucesso.")
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            listar_tarefas(tarefas)
            indice = int(input("Digite o índice da tarefa concluída: "))
            marcar_tarefa_concluida(tarefas, indice)
        elif escolha == '4':
            listar_tarefas(tarefas)
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()