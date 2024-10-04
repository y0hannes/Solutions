# https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        answerString = ''
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] = hashMap[i] + 1
        sortedHashMap = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        for char, frequency in sortedHashMap:
            answerString = answerString + char * frequency

        return answerString