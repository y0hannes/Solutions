# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range = high - low + 1
        if range % 2 == 0:
            return range // 2
        else:
            if low % 2 != 0 or high % 2 != 0:
                return range // 2 + 1
            else:
                return range // 2
