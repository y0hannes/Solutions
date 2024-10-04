# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suffix = total = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            if i != 0:
                prefix += nums[i - 1]
            suffix = total - prefix - nums[i]

            if prefix == suffix:
                return i
        return -1