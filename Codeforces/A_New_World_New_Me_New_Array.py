import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))

def solve():
    n, k, p = read_tup()
    if k == 0:
        print(0)
        return
    q, r = divmod(abs(k), p)
    op = q + 1 if r else q

    if n >= op:
        print(op)
    else:
        print(-1)

def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()