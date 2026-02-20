class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        n = len(s)
        for val in list(c.keys()):
            c[val] -= 1
            n -= 2 * (c[val]//2)
        return n