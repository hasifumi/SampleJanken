#coding:UTF-8

import math

class Player():

    STONE = 0     # グー
    SCISSORS = 1  # チョキ
    PAPER = 2     # パー

    def __init__(self, name):
        self.name = name
        self.winCount = 0

    def showHand(self):
        rand = random.randrange(0, 2)
        print("showHand() has a rand = " + rand)
        if rand == 0:
            return STONE
        elif rand == 1:
            return SCISSORS
        else:
            return PAPER

    def notifyResult(self, result):
        if result == True:
            self.winCount += 1

    def getName(self):
        return self.name

    def getWinCount(self):
        return self.winCount

class Judge():
    def startJanken(self, player1, player2):
        print("start Janken !" + "\n")

        for i in [0, 1, 2]:
            print("Round " + str(i))
            winner = self.judgeJanken(player1, player2)
            if winner != None:
                print(winner.getName() + " wins." + "\n")
                winner.notifyResult(True)
            else:
                print("no winner.")

        print("finished !!" + "\n")

        finalWinner = self.judgeFinalWinner(player1, player2)
        print(str(player1.getWinCount()) + " vs " + str(player2.getWinCount()))
        if finalWinner != None:
            print(finalWinner.getName() + " is a winner.")
        else:
            print("no winner")

    def judgeJanken(self, player1, player2):
        return player1

    def judgeFinalWinner(self, player1, player2):
        if player1.getWinCount() > player2.getWinCount():
            return player1
        elif player2.getWinCount() > player1.getWinCount():
            return player2
        else:
            return None

class ObjectJanken():
    def __init__(self):
        judge = Judge()
        p1 = Player('murata')
        print("Player1's name is " + p1.getName())
        p2 = Player('yamada')
        print("Player2's name is " + p2.getName() + "\n")
        judge.startJanken(p1, p2)


ObjectJanken()

