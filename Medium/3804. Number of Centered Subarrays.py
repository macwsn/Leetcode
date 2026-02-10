class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = n
        for start in range(n):
            for end in range(start+1,n):
                x = nums[start:end+1]
                if sum(x) in x: cnt += 1
        return cnt 