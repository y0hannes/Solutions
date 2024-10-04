# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            reversed_x = int('-' + str(-x)[::-1])
        else:
            reversed_x = int(str(x)[::-1])
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        else:
            return reversed_x