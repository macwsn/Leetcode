class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        d = []
        if len(nums) < 2 or k == 0: return nums
        for i in range(len(nums)):
            if nums[i] >= 0: d.append(nums[i])
        if len(d) == 0: return nums
        a = k % len(d)
        d = d[a:] + d[:a]
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = d[j]
                j += 1
        return nums  