# https://leetcode.com/problems/watering-plants-ii/description/

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i = count = 0
        j = len(plants) - 1
        tempA, tempB = capacityA, capacityB

        while i < j:
            if tempA < plants[i]:
                tempA = capacityA
                count += 1
            tempA -= plants[i]
            i += 1

            if tempB < plants[j]:
                tempB = capacityB
                count += 1
            tempB -= plants[j]
            j -= 1

        if i == j and max(tempA, tempB) < plants[i]:
            count += 1
        return count