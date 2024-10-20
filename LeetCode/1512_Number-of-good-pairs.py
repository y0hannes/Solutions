# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        res = 0
        for n in seen.values():
            if n >= 2:
                res += (n * (n - 1) // 2)

        return res
        