import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))
mod = 10 ** 9 + 7

def solve():
    n = read_int()
    pro = (n * (n + 1) * (2 * n + 1)) // 6
    n -= 1
    pro += (n * ( n + 1) * ( n + 2)) // 3
    pro *= 2022
    pro %= mod
    pro %= mod
    print(pro)

def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()