import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
#TOKEN = '6ce9df5f86a985c5c4d3e3a8f8a56894'
HEADERS = {'Content-type':'application/json','trainer_token': '6ce9df5f86a985c5c4d3e3a8f8a56894'}

def test_status_code():
    responce = requests.get(url= f'{URL}/trainers')
    assert responce.status_code == 200


def test_part_of_response():
    responce = requests.get(url= f'{URL}/trainers', params= {"trainer_id":2122})
    assert responce.json()["data"][0]['trainer_name'] == 'Nastya'
