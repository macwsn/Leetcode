class Solution(object):
    def totalHammingDistance(self, nums):
        cnt = 0
        T = [0 for _ in range(len(bin(max(nums)))-2)]
        for v in nums:
            x = bin(v)
            for i in range(len(x)-1,1,-1):
                if x[i] == '1': T[len(x)-1-i] += 1
        for i in range(len(T)):
            cnt += T[i] * (len(nums)-T[i]) 
        return cnt
        