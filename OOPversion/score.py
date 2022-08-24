class Score:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
        self.score = 0

    def rank_and_score(self):
        eyes_sum = self.first + self.second + self.third

        # pinzoro
        if eyes_sum == 3:
            score = 5
            rank_name = "pinzoro"
            self.score += score
            return f"{rank_name}, 주사위 눈의 합은 {eyes_sum}, 점수 {score} 점."

        # arashi
        if self.first == self.second and self.first == self.third and self.second == self.third:
            if eyes_sum == 3:
                score = 3
                rank_name = "arashi"
                self.score += score
                return f"{rank_name}, 주사위 눈의 합은 {eyes_sum}, 점수 {score} 점."

        # shigoro
        if self.first != self.second and self.first != self.third and self.second != self.third:
            if eyes_sum == 15:
                score = 2
                rank_name = "shigoro"
                self.score += score
                return f"{rank_name}, 주사위 눈의 합은 {eyes_sum}, 점수 {score} 점."

        # machime
        if self.first == self.second or self.first == self.third or self.second == self.third:
            if not self.first == self.second == self.third:
                score = 1
                rank_name = "machime"
                self.score += score
                return f"{rank_name}, 주사위 눈의 합은 {eyes_sum}, 점수 {score} 점."

        # hihumi
        if self.first != self.second and self.first != self.third and self.second != self.third:
            if eyes_sum == 6:
                score = -2
                rank_name = "hihumi"
                self.score += score
                return f"{rank_name}, 주사위 눈의 합은 {eyes_sum}, 점수 {score} 점."

            # menashi
            else:
                score = -1
                rank_name = "menashi"
                self.score += score
                return f"{rank_name}, 주사위 눈의 합은 {eyes_sum}, 점수 {score} 점."
