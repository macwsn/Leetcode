class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = set()
        j = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in a: break
            else: 
                a.add(nums[i])
                j += 1
        b = (len(nums) - j)
        return b // 3 if b % 3 == 0 else (b // 3) + 1