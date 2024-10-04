# https://leetcode.com/problems/array-partition/description/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mid = 0
        for i in range(0, len(nums), 2):
            mid += nums[i]
        return mid