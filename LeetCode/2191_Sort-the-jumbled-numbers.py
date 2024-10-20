# https://leetcode.com/problems/sort-the-jumbled-numbers/description/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transform( mapping, num):
            result = ''
            for digit in str(num):
                result += (str(mapping[int(digit)]))
            return int(result)
        return sorted(nums, key=lambda x: transform(mapping, x))
