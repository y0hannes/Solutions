# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_ = {}
        res = 0
        j  = 0 

        for i in range(len(s)):
            if s[i] in map_:
                j = max(j, map_[s[i]] + 1)
                
            map_[s[i]] = i
            res = max(res, i - j + 1)
        return res
