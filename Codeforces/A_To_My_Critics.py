import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))

def solve():
    nums = read_list()
    for i in range(3):
        for j in range(i + 1, 3):
            if nums[i] + nums[j] >= 10:
                print('YES')
                return 
    print('NO')


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()