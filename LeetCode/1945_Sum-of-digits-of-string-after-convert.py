class Solution:
    def getLucky(self, s: str, k: int) -> int:    
        st = ""
        for i in s:
            st += str(ord(i)-ord('a')+1)
        
        while k > 0:
            res = 0
            for i in st:
                res += int(i)
            st = str(res)
            k -= 1
        
        return res