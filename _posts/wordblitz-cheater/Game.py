import Automate
import Client
from termcolor import colored
import random
import time

class Round:
    def __init__(self):
      self.automate = Automate.Automate()
    
    def setGrid(self, grid):
        self.automate.setGrid(grid)

    def findWordPath(self, words):
        results = []
        for word in words:            
            path = self.automate.findBestWordPath(word)
            path.word = word
            results.append(path)
        results = sorted(results, key=lambda x: x.getPoints(), reverse=True)
        return results
    
    def setBonus(self, bonus):
        self.automate.setBonus(bonus)
    
    def setWords(self, words):
        self.words = []
        for word in words:
             self.words.append(word)

    def getBestWords(self):
        return self.findWordPath(self.words)

    def display(self):
        print('')
        self.automate.displayGrid()
        print('')
        results = self.findWordPath(self.words)
        for path in results:
            print(colored(path.word, 'green') + " " + colored(str(path.getPoints()) + " pts ", 'red') + str(path.path))

class Game:
    def __init__(self):        
        pass

    def setClient(self, client):
        self.client = Client.Client()
    
    def setUsers(self, users):
        self.users = users

    def load(self, game):
        self.gameId = game["id"]
        playersId = game['playerIds']
        self.userId1 = playersId[0]
        self.user1 = self.users[self.userId1]['name']
        self.userId2 = playersId[1]
        self.user2 = self.users[self.userId2]['name']
        userId = self.userId1
        if  userId == self.meId:
            userId = self.userId2
        self.roundIdx = -1
        self.round = None
        self.isRoundAvailable = True
        n = -1
        for round in game['rounds']:
            n = n + 1            
            if 'foundPaths' in round and str(self.meId) in round['foundPaths']:
                if  'foundPaths' in round and str(userId) in round['foundPaths']:
                    self.isRoundAvailable = True
                    continue
                self.isRoundAvailable = False
                continue
            board = round['board']
            bonus = board['boni']
            letters = board['letters']
            words = board['words']
            self.roundIdx = n
            self.round = Round()
            self.round.setGrid(letters)
            self.round.setBonus(bonus)
            self.round.setWords(words)
            break

    
    def isAvailable(self):
        return self.isRoundAvailable

    def display(self):
        self.round.display()

class Games:
    def __init__(self):
        pass

    def setClient(self, client):
        self.client = client
        self.game = []
    
    def load(self):
        self.users = {}
        self.openGames = []
        games = self.client.game_list()
        self.meId = userid = games['user']['id']
        userid = games['user']['id']
        self.users[userid] = games['user']
        for user in games['users']:
            userid = user['id']
            self.users[userid] = user

        for game in games['openGames']:
            gameObj = Game()
            gameObj.setUsers(self.users)
            gameObj.meId = self.meId
            gameObj.load(game)            
            self.openGames.append(gameObj)
    
    def getOpenGames(self):
        return self.openGames




class GamePlay:
    def __init__(self):
        self.client = Client.Client()

    def setToken(self,token):
        self.client.setToken(token)
        self.games = Games()
        self.games.setClient(self.client)

    def play(self):
        while True:
            self.games.load()
            openGames = self.games.getOpenGames()
            availableGames = []
            for game in openGames:
                if game.isAvailable():
                    availableGames.append(game)
            idx = 1
            print("=====================")
            for game in availableGames:
                print("{idx}# - {user1} vs {user2}, round #{round}".format(idx=idx, user1=game.user1, user2=game.user2, round=game.roundIdx+1))
                idx = idx + 1
            print('Select your Game:')
            x = input()
            gameIdx = int(x) - 1
            if gameIdx > (idx-1):
                continue 
            print('(A)utomatic or (M)anual:')
            x = input().upper()
            if x == 'A':
                print("Combien de mots?")
                x = input()
                nbWords = int(x)
                self.automaticGame(availableGames[gameIdx], nbWords)

            if x == 'M':
                availableGames[gameIdx].display()
        
    def automaticGame(self, game, nbWords):
        bestWords = game.round.getBestWords()
        paths = []
        for i in range(nbWords):
            path = []
            for elt in bestWords[i].path:
              path.append(int(elt))  
            paths.append(path)
        self.client.start_game(game.gameId, game.roundIdx)
        print("C'est parti")
        for i in range(81):
            time.sleep(1)
            if i%3 == 0:
                print("\r\r\r.  ", end='')
            if i%3 == 1:
                print("\r\r\r.. ", end='')
            if i%3 == 2:
                print("\r\r\r...", end='')
        self.client.play(game.gameId, game.roundIdx, paths)
