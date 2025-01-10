# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        j, i = len(skill) - 1, 0
        arr = sorted(skill)
        res = arr[i] + arr[j]
        pro = arr[i] * arr[j]
        i += 1
        j -= 1
        while i < j:
            if arr[i] + arr[j] == res:
                pro += (arr[i] * arr[j])
                i += 1
                j -= 1
            else:
                return -1
        return pro