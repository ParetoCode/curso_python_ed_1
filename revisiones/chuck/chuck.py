import requests
from chuck_mocks import example_response

API_URL_RANDOM_JOKE = 'https://api.chucknorris.io/jokes/random'

def request_mock_get():
    return example_response

# Hacer una solicitud GET a la API para obtener un chiste aleatorio
response = requests.get(API_URL_RANDOM_JOKE)

# Extraer el chiste de la respuesta en formato JSON
data = response.json()
joke = data.get('value', 'by default')

# Mostrar el chiste
print(joke)
