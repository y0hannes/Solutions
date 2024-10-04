# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = sorted(nums)
        for i in range(len(arr)):
            if i != arr[i]:
                return i
        return len(nums)