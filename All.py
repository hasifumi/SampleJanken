#coding:UTF-8

import math
import random

class Player():

    STONE = 0     # グー
    SCISSORS = 1  # チョキ
    PAPER = 2     # パー

    def __init__(self, name):
        self.name = name
        self.winCount = 0

    def showHand(self):
        rand = random.randrange(0, 2)
        #print("showHand() has a rand = " + str(rand))
        if rand == 0:
            return self.STONE
        elif rand == 1:
            return self.SCISSORS
        else:
            return self.PAPER

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
                print("no winner." + "\n")

        print("finished !!" + "\n")

        finalWinner = self.judgeFinalWinner(player1, player2)
        print(str(player1.getWinCount()) + " vs " + str(player2.getWinCount()))
        if finalWinner != None:
            print(finalWinner.getName() + " is a winner.")
        else:
            print("no winner")

    def judgeJanken(self, player1, player2):
        player1hand = player1.showHand()
        player2hand = player2.showHand()
        print(self.printHand(player1hand) + " vs " + self.printHand(player2hand))
        #if player1hand == Player.STONE and player2hand == Player.SCISSORS:
        if (player1hand == Player.STONE and player2hand == Player.SCISSORS) or \
           (player1hand == Player.SCISSORS and player2hand == Player.PAPER) or \
           (player1hand == Player.PAPER and player2hand == Player.STONE):
               winner = player1
        elif (player2hand == Player.STONE and player1hand == Player.SCISSORS) or \
             (player2hand == Player.SCISSORS and player1hand == Player.PAPER) or \
             (player2hand == Player.PAPER and player1hand == Player.STONE):
                 winner = player2
        else:
            winner = None
        return winner

    def printHand(self, hand):
        if hand == Player.STONE:
            return "STONE"
        elif hand == Player.SCISSORS:
            return "SCISSORS"
        else:
            return "PAPER"


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

