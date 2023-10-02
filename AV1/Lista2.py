#Questão 1
# listaNotas = []

# while True:
#     nota = float(input("Digite uma nota: "))
#     listaNotas.append(nota)
#     pergunta = input('Quer digitar mais notas?(sim/nao) ')
#     if pergunta == 'sim':
#         continue
#     elif pergunta == 'nao':
#         break
#     else:
#         while (pergunta != 'sim' and pergunta != 'nao'):
#             if (input('Insira uma resposta valida: ') == 'sim'):
#                 break
#             elif (input('Insira uma resposta valida: ') == 'nao'):
#                 continue
#             else:
#                 continue

# if len(listaNotas) > 0:
#     soma = sum(listaNotas)
#     media = soma/len(listaNotas)
#     print('A media é: ', media)

# listaNotas = []

# while True:
#     notas = input('Digite uma nota (ou não para sair): ')
#     if notas.lower() == 'nao':
#         break
#     notas = float(notas)
#     listaNotas.append(notas)

# if len(listaNotas) > 0:
#     soma = sum(listaNotas)
#     media = soma/len(listaNotas)
#     print('A media é: ', media)
# else:
#     print('não tem nota')

listaNotas = []

while True:
    nota = float(input("Digite uma nota: "))
    listaNotas.append(nota)
    
    while True:
        pergunta = input('Quer digitar mais notas? (sim/nao) ')
        if pergunta.lower() == 'sim' or pergunta.lower() == 'nao':
            break
        else:
            print('Resposta inválida. Por favor, digite "sim" ou "nao".')
    
    if pergunta.lower() != 'sim':
        break

if listaNotas:
    soma = sum(listaNotas)
    media = soma / len(listaNotas)
    print('A média é:', media)