# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        map_ = {}
        count = 0
        for i in nums:
            if i in map_:
                map_[i] += 1
            else:
                map_[i] = 1
        for i in map_.values():
            count += i // 3 
            if i == 1:
                return -1
            if i % 3 != 0:
                count += 1
        return count