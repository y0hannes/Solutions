import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))

def solve():
    n = read_int()
    s = read_str()
    up, down = 0, 0
    for ch in s:
        if ch == '-':
            up += 1
        else:
            down += 1
    
    if not down or up < 2:
        print(0)
        return
    q, r = divmod(up, 2)
    if r:
        print((q) * (q + 1) * (down))
    else:
        print( q * q * down)


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()