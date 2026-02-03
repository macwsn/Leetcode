class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        nums[queries[0][1]] += queries[0][0]
        x = 0
        for v in nums: x += v if v % 2 == 0 else 0
        res = [x]
        for i in range(1,n):
            val,idx = queries[i]
            if nums[idx] % 2 == 0:
                if val % 2 == 0:
                    x += val
                else: x -= nums[idx]
            else:
                if val % 2 == 1:
                    x += (val + nums[idx])
            res.append(x)
            nums[idx] += val
        return res
                