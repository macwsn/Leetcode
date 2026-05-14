class Solution:
    def minimumLength(self, s: str) -> int:
        T = []
        n = len(s)
        i = 0
        while i < n:
            j = 1
            while i + j < n and s[i] == s[i+j]: j += 1
            T.append((s[i],i,i+j))
            i += j
        left = 0
        right = len(T) - 1
        while T[left][0] == T[right][0] and left < right:
            left += 1
            right -= 1
        if left == right and T[left][2] - T[left][1] > 1: return 0
        return max(T[right][2] - T[left][1], 0)