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
    nums = read_list()
    nums.sort()
    dis = 1
    wind = 1
    for i in range(1, n):
        diff = abs(nums[i] - nums[i - 1])
        if diff <= k:
            wind += 1
        else:
            dis = max(dis, wind)
            wind = 1
    dis = max(dis, wind)
    print(n - dis)

def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()