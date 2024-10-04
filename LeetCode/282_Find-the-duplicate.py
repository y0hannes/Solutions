# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = [0] * (len(nums))
        for num in nums:
            freq[num - 1] += 1
            if freq[num - 1] > 1:
                return num