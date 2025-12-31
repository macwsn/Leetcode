class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        T = [0]
        for i in range(len(arr)): T.append(T[-1]^arr[i])
        res = []
        for l,r in queries: res.append(T[l]^T[r+1])
        return res