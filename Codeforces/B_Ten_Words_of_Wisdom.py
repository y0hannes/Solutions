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
    data = []
    for _ in range(n):
        data.append(read_tup())
    
    max_quality = 0
    res = -1
    for i, ele in enumerate(data):
        l, q = ele
        if l <= 10 and q > max_quality:
            res = i + 1
            max_quality = q
        
    print(res)


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()