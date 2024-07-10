# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max = 0
        base = len(piles) // 3
        while base < len(piles):
            max += piles[base]
            base += 2
        return max