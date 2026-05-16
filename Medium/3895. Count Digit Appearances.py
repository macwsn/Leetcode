class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        cnt = 0
        for number in nums:
            while number > 0:
                if number % 10 == digit: cnt += 1
                number //= 10
        return cnt