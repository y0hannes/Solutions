# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        my = set()

        for i in nums:
            if i > 0 and i not in my:
                my.add(i)
        
        x = 1
        while(True):
            if x not in my:
                return x
            x += 1