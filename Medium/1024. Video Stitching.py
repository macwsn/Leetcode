class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        d = dict()
        for clip in clips:
            for i in range(clip[0] + 1,clip[1] + 1):
                if i not in d: d[i] = set()
                d[i].add(clip[0])
        dp = [0 for _ in range(time+1)]
        for i in range(1, time+1):
            mi = float('inf')
            if i not in d: return -1
            for val in d[i]: mi = min(mi, dp[val] + 1)
            dp[i] = mi
        return dp[-1]