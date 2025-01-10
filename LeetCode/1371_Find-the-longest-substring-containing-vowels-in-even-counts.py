# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {
            'a' : 1,
            'e' : 2,
            'i' : 4,
            'o' : 8,
            'u' : 16
        }
        res = 0
        mask = 0
        mask_to_index = [-1] * 32
        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ vowels[c]
            if mask_to_index[mask] != -1 or mask == 0:
                res = max(res, i - mask_to_index[mask])
            else:
                mask_to_index[mask] = i
        return res
