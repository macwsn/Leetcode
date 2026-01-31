class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        T = []
        for i in range(1,len(nums)): T.append(nums[i] - nums[i-1])
        T.append(float('inf'))
        i = 0
        cnt = 0
        while i < len(nums):
            j = 1
            while i + j < len(T) and T[i+j] == T[i]: j += 1
            i += j
            cnt += (j-1)*j // 2
        return cnt