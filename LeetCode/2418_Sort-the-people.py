# https://leetcode.com/problems/sort-the-people/description/


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map_ = {}
        for h, name in zip(heights, names):
            map_[h] = name

        res = [map_[h] for h in (sorted(map_.keys(), reverse= True))]
        return res