import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))

def solve():
    n, k, m = read_tup()
    nums = read_list()
    nums.sort()
    if n == 1:
        print(1)
        return
    diffs = []

    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        if diff > m:
            diffs.append(diff)
    diffs.sort()

    res = len(diffs) + 1
    for i in range(len(diffs)):
        temp = (diffs[i] - 1 )// m
        if k >= temp:
            k -= temp
            res -= 1
        else:
            break
    print(res)


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()