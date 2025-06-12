import requests

def chamar_api_eteros():
    url = "https://api.eteros.io/v1/endpoint"  # Substitua pelo endpoint correto da API

    headers = {
        "Authorization": "Bearer SEU_TOKEN_AQUI",  # Coloque seu token real aqui
        "Content-Type": "application/json"
    }

    payload = {
        "param1": "valor1",
        "param2": "valor2"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Vai gerar erro se o status não for 200
        dados = response.json()
        print("Resposta da API:", dados)
        return dados
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro inesperado:", err)

if __name__ == "__main__":
    chamar_api_eteros()
