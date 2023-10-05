#Questão 1

# def calcula_media(notas):
#     if notas:
#         soma = sum(notas)
#         media = soma / len(notas)
#         return media
#     else:
#         return None

# listaNotas = []

# while True:
#     nota = float(input("Digite uma nota: "))
#     listaNotas.append(nota)
    
#     while True:
#         pergunta = input('Quer digitar mais notas? (sim/nao) ')
#         if pergunta.lower() == 'sim' or pergunta.lower() == 'nao':
#             break
#         else:
#             print('Resposta inválida. Por favor, digite "sim" ou "nao".')
    
#     if pergunta.lower() != 'sim':
#         break

# media = calcula_media(listaNotas)

# if media is not None:
#     print('A média é:', media)
# else:
#     print('Nenhuma nota foi inserida.')

#Questão 2

# import csv
# import os

# def criar_agenda(arquivo_csv):
#     if not os.path.exists(arquivo_csv):
#         with open(arquivo_csv, 'w', newline='') as arquivo:
#             cabecalho = ['Nome', 'Telefone', 'Email']
#             escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)
#             escritor_csv.writeheader()

# def adicionar_contato(arquivo_csv, nome, telefone, email):
#     with open(arquivo_csv, 'a', newline='') as arquivo:
#         escritor_csv = csv.DictWriter(arquivo, fieldnames=['Nome', 'Telefone', 'Email'])
#         escritor_csv.writerow({'Nome': nome, 'Telefone': telefone, 'Email': email})
#     print(f"Contato {nome} adicionado com sucesso!")

# def listar_contatos(arquivo_csv):
#     with open(arquivo_csv, 'r') as arquivo:
#         leitor_csv = csv.DictReader(arquivo)
#         for linha in leitor_csv:
#             print(f"Nome: {linha['Nome']}, Telefone: {linha['Telefone']}, Email: {linha['Email']}")

# def buscar_contato(arquivo_csv, nome):
#     with open(arquivo_csv, 'r') as arquivo:
#         leitor_csv = csv.DictReader(arquivo)
#         encontrado = False
#         for linha in leitor_csv:
#             if linha['Nome'] == nome:
#                 print(f"Nome: {linha['Nome']}, Telefone: {linha['Telefone']}, Email: {linha['Email']}")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print(f"Contato com o nome {nome} não encontrado.")

# def remover_contato(arquivo_csv, nome):
#     with open(arquivo_csv, 'r') as arquivo:
#         contatos = list(csv.DictReader(arquivo))
    
#     encontrado = False
#     for contato in contatos:
#         if contato['Nome'] == nome:
#             contatos.remove(contato)
#             encontrado = True
#             break
    
#     if encontrado:
#         with open(arquivo_csv, 'w', newline='') as arquivo:
#             cabecalho = ['Nome', 'Telefone', 'Email']
#             escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)
#             escritor_csv.writeheader()
#             for contato in contatos:
#                 escritor_csv.writerow(contato)
#         print(f"Contato {nome} removido com sucesso!")
#     else:
#         print(f"Contato com o nome {nome} não encontrado.")

# if __name__ == "__main__":
#     arquivo_csv = 'agenda.csv'
#     criar_agenda(arquivo_csv)

#     while True:
#         print("\nOpções:")
#         print("1. Adicionar contato")
#         print("2. Listar contatos")
#         print("3. Buscar contato")
#         print("4. Remover contato")
#         print("5. Sair")

#         escolha = input("Escolha uma opção: ")

#         if escolha == '1':
#             nome = input("Nome: ")
#             telefone = input("Telefone: ")
#             email = input("Email: ")
#             adicionar_contato(arquivo_csv, nome, telefone, email)
#         elif escolha == '2':
#             listar_contatos(arquivo_csv)
#         elif escolha == '3':
#             nome = input("Digite o nome do contato a ser buscado: ")
#             buscar_contato(arquivo_csv, nome)
#         elif escolha == '4':
#             nome = input("Digite o nome do contato a ser removido: ")
#             remover_contato(arquivo_csv, nome)
#         elif escolha == '5':
#             print("Saindo do programa.")
#             break
#         else:
#             print("Opção inválida. Por favor, escolha uma opção válida.")

#Questão 3

import random

def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Dica: É uma palavra com", len(palavra), "letras.")
    
    while True:
        palavra_mostrada = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_mostrada += letra
            else:
                palavra_mostrada += "_"
        
        print("\nPalavra: " + palavra_mostrada)
        print("Tentativas restantes:", tentativas)
        
        if palavra_mostrada == palavra:
            print("Parabéns, você venceu! A palavra é:", palavra)
            break
        
        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break
        
        letra_palpite = input("Digite uma letra: ").lower()
        
        if len(letra_palpite) != 1 or not letra_palpite.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue
        
        if letra_palpite in letras_corretas:
            print("Você já tentou esta letra antes.")
        elif letra_palpite in palavra:
            letras_corretas.append(letra_palpite)
        else:
            print("Letra errada!")
            tentativas -= 1 

if __name__ == "__main__":
    jogar_forca()