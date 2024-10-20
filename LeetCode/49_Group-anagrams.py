# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = {}
        for s in strs:
            x = tuple(sorted(s))
            if x in mapped:
                mapped[x].append(s)
            else:
                mapped[x] = [s]
            
        return list(mapped.values())