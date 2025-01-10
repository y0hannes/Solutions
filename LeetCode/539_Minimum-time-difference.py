# https://leetcode.com/problems/minimum-time-difference/description/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = [0]* len(timePoints)
        i = 0

        for timePoint in timePoints:
            h, m = map(int, timePoint.split(':'))
            time[i] = h*60 + m
            i += 1
        
        minDiff = 1440
        time.sort()
        for i in range(len(time) - 1):
            diff = time[i+1] - time[i]
            if diff < minDiff:
                minDiff = diff
        diff = time[0] - time[-1] + 1440
        if diff < minDiff:
            minDiff = diff

        return minDiff
