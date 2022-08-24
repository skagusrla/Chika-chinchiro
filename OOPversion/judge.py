class Judge:
    def __init__(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def judge(self):
        if self.player1_score > self.player2_score:
            return "player1 승리"
        if self.player1_score < self.player2_score:
            return "player2 승리"
        else:
            return "무승부"
