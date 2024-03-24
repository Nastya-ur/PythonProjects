import requests

#{'id': '2122', 'trainer_token': '6ce9df5f86a985c5c4d3e3a8f8a56894', 'trainer_name': 'Nastya'}
#wutrussixoutoi-7494@yopmail.com
#K1234567890


URL = 'https://api.pokemonbattle.me/v2'
#TOKEN = '6ce9df5f86a985c5c4d3e3a8f8a56894'
HEADERS = {'Content-type':'application/json','trainer_token': '6ce9df5f86a985c5c4d3e3a8f8a56894'}

"""body = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}"""

"""body_put = {
    "pokemon_id": "14746",
    "name": "Bebe QA",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}"""

body_addpokeball = {
    "pokemon_id": "14746"
}


"""response = requests.post(url= f'{URL}/pokemons', headers= HEADERS, json= body)
print(response.text)"""

#{"message":"Покемон создан","id":"14746"}

"""response = requests.put(url= f'{URL}/pokemons', headers= HEADERS, json= body_put)
print(response.text)"""

#{"message":"Информация о покемоне обновлена","id":"14746"}

response = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADERS, json= body_addpokeball)
print(response.text)

#{"message":"Покемон пойман в покебол","id":"14746"}
