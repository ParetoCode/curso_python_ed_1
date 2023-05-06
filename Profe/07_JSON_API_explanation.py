# REST, APIS

# GET, DELETE, POST, PUT, PATCH

# GET, DELETE
"obtener datos o borrar datos, no manda datos con json solo query param " 
"www.whatever.com/users?name=jorge&age=29"

# POST -> CREAR
"www.whatever.com/users/"
'{"name": "Joselyn", "age":"dontAsk"}'

# PUT -> MODIFICAR
"www.whatever.com/users?name=joselyn"
'{"age": "Taitantos"}'

# PATCH -> MODIFICAR
"www.whatever.com/users?name=joselyn"
'{"name": "Joselyn", "age":"21"}'

import json

# JSON FORMAT not depending on me
pokemon_response = '{"name": "Pikachu", "power": "Electricity"}'

###

pokemon = json.loads(pokemon_response)

assert type(pokemon) == dict
print(pokemon)