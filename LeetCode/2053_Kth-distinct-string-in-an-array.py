# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map_ = {}
        for s in arr:
            if s in map_:
                map_[s] += 1
            else:
                map_[s] = 1
        
        count = 0
        for m, v in map_.items():
            if v == 1:
                count +=1
                if count == k:
                    return m
        return ''