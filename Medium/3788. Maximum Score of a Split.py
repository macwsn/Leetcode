class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        P = [nums[0]]
        for i in range(1,len(nums)): P.append(P[i-1] + nums[i])
        S = [P[-1]]*len(nums)
        S[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1): S[i] = nums[i] if S[i+1] > nums[i] else S[i+1]
        m = float('-inf')
        for i in range(len(nums)-1):
            if P[i] - S[i+1] > m: m = P[i] - S[i+1]
        return m