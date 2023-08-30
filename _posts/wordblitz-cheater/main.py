#!python3.10
import json
import Game


def main():
    f = open('config.json')
    config = json.load(f)
    gp = Game.GamePlay()
    gp.setToken(config['signature'])
    gp.play()
main()