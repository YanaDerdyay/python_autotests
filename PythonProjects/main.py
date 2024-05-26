import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '368ac0a2004ef47362319e2f4f878fa3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_creation = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "pokemon_id": "28432",
    "name": "Бульбазавр New",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_pokeball = {
    "pokemon_id": "28432"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)