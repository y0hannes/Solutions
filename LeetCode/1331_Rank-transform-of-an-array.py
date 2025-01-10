# https://leetcode.com/problems/rank-transform-of-an-array/description/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        values = sorted(set(arr))
        map_ = {val : i + 1 for i, val in enumerate(values)}
        
        for i in range(len(arr)):
            arr[i] = map_[arr[i]]        
        return arr