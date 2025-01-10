# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminders = {}
        for i in arr:
            rem = (i % k + k) % k
            reminders[rem] = reminders.get(rem, 0) + 1
        
        for rem in reminders:
            if rem == 0:
                if reminders[rem] % 2 != 0:
                    return False
            else:
                counter = k - rem
                if reminders[rem] != reminders.get(counter, 0):
                    return False
        return True