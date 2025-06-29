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
    if not n & 1:
        print('YES')
    else:
        if (n - k) & 1:
            print('NO')
        else:
            print('YES')


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()