class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(base:int, n:int):
            s = []
            i = base
            while n > 0:
                s.append(n%i)
                n //= base
            return s
        for i in range(2,n-1):
            x = convert(i,n)
            if x != x[::-1]: return False
        return True

