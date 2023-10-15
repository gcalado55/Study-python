import random

def escolher_palavra():
    with open("D:/GitHub/studies-python/AV1/Lista 2/palavras.txt", "r") as arquivo:
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