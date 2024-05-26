import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '368ac0a2004ef47362319e2f4f878fa3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '2327'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['id'] == TRAINER_ID

