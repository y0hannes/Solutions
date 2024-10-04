# https://leetcode.com/problems/majority-element-ii/description/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        min = len(nums) //3
        counts = Counter(nums)
        res = [num for num, count in counts.items() if count > min]
        return res