# https://leetcode.com/problems/count-primes/description/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2
        while (p * p <= n):
            if is_prime[p] == True:
                for i in range(p*p, n, p):
                    is_prime[i] = False
            p += 1
        
        primes = 0

        for i in range(2, n):
            if is_prime[i] == True:
                primes += 1
        return primes