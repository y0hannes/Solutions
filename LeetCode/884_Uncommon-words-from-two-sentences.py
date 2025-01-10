# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        count = Counter(words)
        ans = [x for x in count if count[x] == 1]
        return ans