# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()
        return len(string[-1])