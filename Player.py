#coding:UTF-8

import math

class Player():

    STONE = 0     # グー
    SCISSORS = 1  # チョキ
    PAPER = 2     # パー

    def __init__(self, name):
        self.name = name
        self.winCount = 0

    def showHand():
        rand = random.randrange(0, 2)
        print("showHand() has a rand = " + rand)
        if rand == 0:
            return STONE
        elif rand == 1:
            return SCISSORS
        else:
            return PAPER

    def notifyResult(result):
        if result == True:
            self.winCount += 1

    def getName():
        return self.name

    def getWinCount():
        return self.winCount
