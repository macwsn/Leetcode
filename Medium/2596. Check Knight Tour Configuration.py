class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        n = len(height)
        start = 0
        end = n - 1
        while start < end:
            m = max(m, (end - start) * min(height[start],height[end]))
            if height[start] > height[end]: end -= 1
            else: start += 1
        return m