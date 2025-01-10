# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []
        i = 0
        res = [[0] * n for _ in range(m)]
        for j in range(m):
            for k in range(n):
                res[j][k] = original[i]
                i += 1
        
        return res