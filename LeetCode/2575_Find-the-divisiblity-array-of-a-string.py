# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description/

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        curr = 0 
        res = [0] * len(word)
        for i in range(len(word)):
            curr = (curr * 10 + int(word[i])) % m
            if curr == 0:
                res[i] = 1

        return res
            