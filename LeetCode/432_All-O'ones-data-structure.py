# https://leetcode.com/problems/all-oone-data-structure/description/

class AllOne:
    def __init__(self):
        self.keyCount = {}
        self.countKeys = {}
        self.maxCount = 0
        self.minCount = float('inf')

    def inc(self, key: str) -> None:
        count = self.keyCount.get(key, 0)
        new_count = count + 1
        self.keyCount[key] = new_count

        if count > 0:
            if key in self.countKeys[count]:
                self.countKeys[count].remove(key)
                if not self.countKeys[count]:
                    del self.countKeys[count]
                    if count == self.minCount:
                        self.minCount += 1  

        if new_count not in self.countKeys:
            self.countKeys[new_count] = set()
        self.countKeys[new_count].add(key)

        self.maxCount = max(self.maxCount, new_count)
        self.minCount = min(self.minCount, new_count)
        if self.minCount == float('inf'):
            self.minCount = new_count  

    def dec(self, key: str) -> None:
        if key not in self.keyCount:
            return

        count = self.keyCount[key]
        new_count = count - 1
        
        if key in self.countKeys[count]:
            self.countKeys[count].remove(key)
            if not self.countKeys[count]:
                del self.countKeys[count]
                if count == self.maxCount:
                    self.maxCount -= 1  

        if new_count == 0:
            del self.keyCount[key]
            if count == self.minCount and key not in self.keyCount:
                self.minCount = min(self.countKeys.keys(), default=float('inf'))
        else:
            self.keyCount[key] = new_count
            if new_count not in self.countKeys:
                self.countKeys[new_count] = set()
            self.countKeys[new_count].add(key)

            self.minCount = min(self.minCount, new_count)
            self.maxCount = max(self.maxCount, new_count)

    def getMaxKey(self) -> str:
        if self.maxCount == 0:
            return ""
        return next(iter(self.countKeys[self.maxCount]))

    def getMinKey(self) -> str:
        if self.minCount == float('inf'):
            return ""
        return next(iter(self.countKeys[self.minCount]))
