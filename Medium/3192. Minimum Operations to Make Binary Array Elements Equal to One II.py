class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 1 if nums[0] == 0 else 0
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] != nums[i]: cnt += 1
        return cnt