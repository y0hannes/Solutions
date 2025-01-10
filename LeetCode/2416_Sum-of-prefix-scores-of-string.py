# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Trie:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()

        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Trie()
                curr = curr.children[ch]
                curr.prefix_count += 1

        ans = []
        for word in words:
            curr = root
            temp = 0
            for ch in word:
                curr = curr.children[ch]
                temp += curr.prefix_count
            ans.append(temp)
        return ans
