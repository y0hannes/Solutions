# https://leetcode.com/problems/height-checker/description/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        sum = 0
        for i in range(len(heights)):
            if temp[i] != heights[i]:
                sum += 1
        return sum