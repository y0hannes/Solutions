# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [len(s)] * (len(s) + 1)
        dp[0] = 0
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in words:
                    dp[i] = min(dp[i], dp[j])
            dp[i] = min(dp[i], dp[i - 1] + 1)

        return True if dp[i] == 0 else False