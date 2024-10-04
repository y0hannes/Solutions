# https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        merged = []
        i, j = 0, 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1
        
        merged.extend(left_half[i:])
        merged.extend(right_half[j:])
        
        return merged
        