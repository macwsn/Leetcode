class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        cnt = 0
        s = dict()
        for a, b in reservedSeats: 
            if a-1 in s: s[a-1].append(b-1)
            else: s[a-1] = [b-1]
        X = list(s.keys())
        for i in X:
            T = [0 for _ in range(10)]
            for v in s[i]: T[v] = 1
            left = T[1]+T[2]+T[3]+T[4] == 0
            mid = T[3]+T[4]+T[5]+T[6] == 0
            right = T[5]+T[6]+T[7]+T[8] == 0
            if left and right: cnt += 2
            elif left or mid or right: cnt += 1
        return cnt + 2 * (n - len(X))