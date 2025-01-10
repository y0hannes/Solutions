# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        set_ = set(allowed)
        for word in words:
            found = True
            for s in word:
                if s not in set_:
                    found = False
                    break
            if found:
                count += 1
        return count