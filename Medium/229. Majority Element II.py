import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = collections.Counter(nums)
        a = len(nums)
        ans = []
        for v in list(x.keys()): 
            if x[v] > a // 3: ans.append(v)
        return ans
#bruteforce