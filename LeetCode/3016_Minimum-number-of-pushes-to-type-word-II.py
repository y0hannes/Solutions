# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/

from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:

        count = Counter(word)
        res = sorted(count.values(), reverse= True)
        return sum(res[:8] * 1 + res[8:16] * 2 + res[16:24] * 3 + res[24: ] * 4) 