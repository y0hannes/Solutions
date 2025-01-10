# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        count = 0
        temp = 0
        for i in nums:
            if i > max_val:
                max_val = i
                count = 1
                temp = 1
            elif i == max_val:
                temp += 1
            else:
                count = max(count, temp)
                temp = 0
        
        count = max(count, temp)
        return count