class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        odd = True
        even = False
        o = 0
        e = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd,even = even,odd
            if i%6 == 5:
                odd,even = even,odd
            if odd: o += nums[i]
            else: e += nums[i]
        return o-e