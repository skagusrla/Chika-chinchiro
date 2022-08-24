from score import Score
from judge import Judge
import random

play1 = Score(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
play2 = Score(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

player1 = play1.rank_and_score()
player2 = play2.rank_and_score()
judge = Judge(play1.score, play2.score)

print(player1)
print(player2)
print(judge.judge())


