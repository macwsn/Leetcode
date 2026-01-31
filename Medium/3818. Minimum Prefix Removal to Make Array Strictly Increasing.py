class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        i = len(nums) - 1
        while i > 0:
            i -= 1
            if nums[i + 1] <= nums[i]: return i + 1
        return 0