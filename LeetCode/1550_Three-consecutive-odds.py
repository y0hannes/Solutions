# https://leetcode.com/problems/three-consecutive-odds/description/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                res += 1
            else:
                res = 0
            if res == 3:
                return True
        return False