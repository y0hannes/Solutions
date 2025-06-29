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
    op = 0
    zeros = 0
    for i in range(1, n):
        while nums[i] <= nums[i - 1]:
            if zeros >= 2:
                print(-1)
                return
            nums[i - 1] //= 2
            if nums[i -1] == 0:
                zeros += 1
            op += 1
        for j in range(i - 1, -1, -1):
            while nums[j - 1] >= nums[j]:
                if zeros >= 2:
                    print(-1)
                    return
                nums[j - 1] //= 2
                if nums[j -1] == 0:
                    zeros += 1
                op += 1
            break
    print(op)


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()