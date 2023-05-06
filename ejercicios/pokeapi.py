import requests
# from pokemon_demo import pokemon

pokemon_id = input('Introduce número de pokemon: ')

BASE_URL = 'https://pokeapi.co/api/v2/'

first_pokemon_url = f'{BASE_URL}pokemon/{pokemon_id}'
first_pokemon_json = requests.get(first_pokemon_url)

first_pokemon = first_pokemon_json.json()

# first_pokemon = pokemon
print(first_pokemon.get('name', 'No existe'))

moves = first_pokemon.get('moves', [])

for move in moves:
    print(move['move']['name'])