# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = min(height[i], height[j]) * (j - i)
        while i < j:
            temp = min(height[i], height[j]) * (j - i)
            if temp > area:
                area = temp
            else:
                if height[i] < height[j]:
                    i += 1
                else:
                    j -= 1
        return area