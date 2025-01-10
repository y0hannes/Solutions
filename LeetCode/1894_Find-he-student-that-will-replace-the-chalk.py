# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]
