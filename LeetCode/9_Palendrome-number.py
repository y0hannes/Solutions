# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_s = str(x)
        return True if num_s == (num_s[::-1]) else False