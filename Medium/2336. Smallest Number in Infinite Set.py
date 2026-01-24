from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.deleted = [float('inf')]
        self.cnt = 1

    def popSmallest(self) -> int:
        if self.deleted[0] < self.cnt: 
            return heappop(self.deleted)
        else:
            self.cnt += 1
            if self.cnt - 1 in self.deleted:
                del self.deleted[self.deleted.index(self.cnt - 1)]
            return self.cnt - 1

    def addBack(self, num: int) -> None:
        if self.cnt <= num: return None
        if num == self.cnt - 1:
            self.cnt -= 1
            return None
        if num not in self.deleted: heappush(self.deleted,num)