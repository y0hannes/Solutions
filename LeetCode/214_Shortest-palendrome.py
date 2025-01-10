# https://leetcode.com/problems/shortest-palindrome/description/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = s + '&' + s[::-1]
        lps = [0] * len(new_s)
        prev = 0
        i = 1

        while i < len(new_s):
            if new_s[prev] == new_s[i]:
                prev += 1
                lps[i] = prev
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev - 1]
        return s[lps[-1]:][::-1] + s