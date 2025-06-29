import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))

def solve():
    n, k = read_tup()
    ans = 0
    if n % 2 == 1:
        n -= k
        ans = 1
    k -= 1
    ans += (n + k - 1) // k
    print(ans)

def main():
    t = read_int()
    for i in range(t):
        solve()

if __name__ == '__main__':
    main()