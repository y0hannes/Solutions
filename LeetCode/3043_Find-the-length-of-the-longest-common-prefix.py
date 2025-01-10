# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        map_ = {}
        for i in arr1:
            prefix = ''
            for ch in str(i):
                prefix += ch
                if prefix in map_:
                    map_[prefix] = max(map_[prefix], len(prefix))
                else:
                    map_[prefix] = len(prefix)
        
        max_len = 0
        for i in arr2:
            prefix =''
            for ch in str(i):
                prefix += ch
                if prefix in map_:
                    max_len = max(max_len, map_[prefix])
        return max_len