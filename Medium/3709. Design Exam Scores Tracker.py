from bisect import bisect_left, bisect_right
class ExamTracker:

    def __init__(self):
        self.scores = [0]
        self.times = []

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.scores.append(score + self.scores[-1])

    def totalScore(self, startTime: int, endTime: int) -> int:
        res = 0
        left = bisect_left(self.times,startTime)
        right = bisect_right(self.times, endTime)
        res = max(self.scores[right] - self.scores[left],0)
        return res
