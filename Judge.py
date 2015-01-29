#coding:UTF-8

class Judge():
    def startJanken(player1, player2):
        print(u"ジャンケン開始！")

        for i in [0, 1, 2]:
            print(u"【" + i + "回戦目】")
            winner = judgeJanken(player1, player2)
            if winner != 0:
                print(winner.getName() + u"さんが勝ちました")
                winner.notifyResult(True)
            else:
                print(u"引き分けです")

        print(u"ジャンケン終了")

        finalWinner = judgeFinalWinner(player1, player2)
        print(player1.getWinCount() + u"対" + player2.getWinCount() + u"で")
        if finalWinner != None:
            print(finalWinner.getName() + u"さんの勝ちです")
        else:
            print(u"引き分けです")
