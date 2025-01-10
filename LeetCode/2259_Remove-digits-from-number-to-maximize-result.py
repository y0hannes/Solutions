# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = ''
        for i in range(len(number)):
            if number[i] == digit:
                temp = number[:i] + number[i+1:]
                ans = max(ans, temp)
        return ans