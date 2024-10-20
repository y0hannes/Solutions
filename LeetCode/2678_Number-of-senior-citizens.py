# https://leetcode.com/problems/number-of-senior-citizens/description/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for data in details:
            if int(data[11: 13]) > 60:
                res += 1
        return res