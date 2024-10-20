# https://leetcode.com/problems/first-unique-character-in-a-string/description/

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for x in range(len(s)):
            if count[s[x]] == 1:
                return x
        return -1