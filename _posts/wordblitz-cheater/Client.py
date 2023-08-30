import requests
import json

class Client:
    def __init__(self):
        self.token = ''
        pass
    def setToken(self, token):
        self.token = token
    
    def game_list(self):
        url = 'https://wordblitz-api-prod.lotum.com/v2/game/list?version=5.115.0&signature=' + self.token
        x = requests.get(url)        
        return json.loads(x.text)

    def start_game(self, gameId, round):
        url = 'https://wordblitz-api-prod.lotum.com/v2/game/start?version=5.115.0&signature=' + self.token
        form_data = {'duration': 80, 'gameId': gameId, 'round': round}
        x = requests.post(url, data = form_data)


    def play(self, gameId, round, paths):
        url = 'https://wordblitz-api-prod.lotum.com' + '/v2/game/play?version=5.115.0&signature=' + self.token
        print("path= " + str(paths))
        words = []
        for path in paths:
            word = json.dumps({"p":path,"o":"u"})
            words.append(word)
        form_data = {'gameId': gameId, 'round': round, 'words': words}
        x = requests.post(url, data = form_data)
        print(x.text)
        



