# 점수, 배율

def score_and_gain(a, b, c):
    score = a + b + c

    # pinzoro
    if score == 3:
        gain = 5
        ranking = "pinzoro"
        return score, gain, ranking

    # arashi
    if a == b and a == c and b == c:
        if score == 3:
            gain = 3
            ranking = "arashi"
            return score, gain, ranking

    # shigoro
    if a != b and a != c and b != c:
        if score == 15:
            gain = 2
            ranking = "shigoro"
            return score, gain, ranking

    # machime
    if a == b or a == c or b == c:
        if not a == b == c:
            gain = 1
            ranking = "machime"
            return score, gain, ranking

    # hihumi
    if a != b and a != c and b != c:
        if score == 6:
            gain = -2
            ranking = "hihumi"
            return score, gain, ranking

    # menashi
        else:
            gain = -1
            ranking = "menashi"
            return score, gain, ranking

