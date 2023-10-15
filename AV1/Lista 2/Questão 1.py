def calcula_media(notas):
    if notas:
        soma = sum(notas)
        media = soma / len(notas)
        return media
    else:
        return None

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

media = calcula_media(listaNotas)

if media is not None:
    print('A média é:', media)
else:
    print('Nenhuma nota foi inserida.')