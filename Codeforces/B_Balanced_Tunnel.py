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
    enter = read_list()
    exited = read_list()
    left, right = 0, 0
    fined = 0

    while right < n:
        if enter[left] != exited[right]:
            fined += 1
            right += 1
        else:
            left += 1
            right += 1
    
    print(fined)


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()