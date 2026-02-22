class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        L = [0 for _ in range(value)]
        for val in nums: L[val % value] += 1
        return L.index(min(L)) + value * min(L)