# https://leetcode.com/problems/find-missing-observations/description/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls)
        res = (mean * (len(rolls) + n)) - (total )
        if int(res) != res:
            return []
        factor = res // n
        m = res % n
        if res < n or res > 6*n:
            return []
        else:
            temp = [factor] * (n - m)
            temp.extend([factor + 1] * m)
        
        return temp