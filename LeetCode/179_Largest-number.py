# https://leetcode.com/problems/largest-number/description/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s_nums = [str(num) for num in nums]
        max_len = max(len(num) for num in s_nums)

        s_nums.sort(key=lambda x : x * max_len, reverse=True)

        if s_nums[0] == '0':
            return '0'
        return ''.join(s_nums)