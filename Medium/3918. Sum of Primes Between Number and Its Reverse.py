class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = int(str(n)[::-1])
        a = min(rev,n)
        b = max(rev,n)
        T = [i for i in range(b+1)]
        P = []
        for i in range(2,len(T)):
            if T[i] != 0: 
                P.append(i)
                for j in range(2*i, len(T), i): T[j] = 0
        del T
        count_start = False
        cnt = 0
        for v in P:
            if v > b: return cnt
            if not count_start and v >= a: count_start = True
            if count_start: cnt += v 
        return cnt