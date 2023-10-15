import requests

def consultar_previsao_tempo(cidade, ace063fdf4f2c0be51af8953779bac08):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={ace063fdf4f2c0be51af8953779bac08}&lang=pt_br&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        
        data = response.json()
        cidade = data["name"]
        temperatura = data["main"]["temp"]
        descricao_clima = data["weather"][0]["description"]
        
        print(f"Previsão do tempo em {cidade}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Clima: {descricao_clima.capitalize()}")
    else:
        print("Não foi possível obter a previsão do tempo para a cidade especificada.")

def main():
    cidade = input("Digite o nome da cidade: ")
    chave_api = "ace063fdf4f2c0be51af8953779bac08"
    consultar_previsao_tempo(cidade, chave_api)

if __name__ == "__main__":
    main()