from statistics import median
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = grid[0][0] % x
        T = [ ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] % x != m: return -1
                grid[i][j] -= m
                grid[i][j] //= x
                T.append(grid[i][j])
        # mamy jedynki
        val = median(T)
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt += abs(grid[i][j] -  val)
        return int(cnt)