# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = time % (2 * (n - 1))
        if x > n - 1:
            return n - (x - (n - 1))
        else:
            return x + 1