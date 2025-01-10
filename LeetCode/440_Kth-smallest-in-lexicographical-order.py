# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def helper(left):
            steps = 0
            right = left + 1
            while left <= n:
                steps += min(right, n + 1) - left
                left *= 10
                right *= 10
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = helper(curr)
            if k >= steps:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        
        return curr