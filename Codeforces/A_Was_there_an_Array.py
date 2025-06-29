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
    nums = read_list()

    if len(nums) < 3:
        print('YES')
        return
    
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 0 and nums[i+ 2] == 1:
            print('NO')
            return 
    print('YES')


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()