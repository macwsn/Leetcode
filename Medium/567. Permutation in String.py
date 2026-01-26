from collections import Counter
from copy import deepcopy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        for start in range(len(s2) - len(s1)+1):
            c2 = Counter(s2[start:start+len(s1)])
            if c2 == c: return True
        return False