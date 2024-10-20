# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in map_:
                return [map_[x], i]
            else:
                map_[nums[i]] = i