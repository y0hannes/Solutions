# https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for n in bills:
            if n == 5:
                five += 1
            elif n == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif n == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
            