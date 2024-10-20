# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = count = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1
            
            res = max(res, j - i + 1)
        return res