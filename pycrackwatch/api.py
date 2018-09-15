import requests
from .models import Crack, Game

_base_url = 'http://api.crackwatch.com/api/{}'


def getCracks():
    url = _base_url.format('cracks')
    req = requests.get(url)
    json_list = req.json()

    crack_list = []

    for j in json_list:
        crack = Crack(j)
        crack_list.append(crack)

    return crack_list


def getGames():
    url = _base_url.format('games')
    req = requests.get(url)
    json_list = req.json()

    game_list = []

    for j in json_list:

        game = Game(j)
        game_list.append(game)

    return game_list
