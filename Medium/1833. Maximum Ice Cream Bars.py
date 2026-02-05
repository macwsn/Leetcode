class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = [0 for _ in range(max(costs)+1)]
        for v in costs: n[v] += 1
        i = 1
        res = 0
        while i < len(n) and coins > 0:
            if n[i] == 0: i += 1
            else:
                x = coins // i 
                if x == 0: return res
                coins -= min(x,n[i]) * i
                res += min(x,n[i])
                i += 1
        return res
