# https://leetcode.com/problems/extra-characters-in-a-string/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)

        prefix = [len(s)] * (len(s) + 1)
        prefix[0] = 0

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in words:
                    prefix[i] = min(prefix[i], prefix[j])
                    
            prefix[i] = min(prefix[i], prefix[i - 1] + 1)

        return prefix[i]