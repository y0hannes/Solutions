# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        j = num
        while i <= j:
            x = (i + j)// 2
            if x * x == num:
                return True
            elif x * x < num:
                i = x + 1
            else:
                j = x - 1
        
        return False