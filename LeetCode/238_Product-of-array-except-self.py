# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        r = 0
        while(r < len(nums)):
            prefix.append(prefix[r] * nums[r]) 
            r += 1
            
        suffix  = [1] * len(nums)

        for i in range(len(nums), 1, -1):
            suffix[i - 2] = suffix[i - 1] * nums[i - 1]

        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]

        return nums