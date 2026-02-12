from collections import Counter
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        x = Counter(nums)
        y = x.keys()
        z = dict()
        for v in y:
            if x[v] in z: z[x[v]] += 1
            else: z[x[v]] = 1
        res = -1
        for val in nums:
            if z[x[val]] == 1: return val
        return res