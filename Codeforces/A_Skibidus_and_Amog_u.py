import sys
import math
import bisect
from collections import Counter, defaultdict

def read_int(): return int(sys.stdin.readline().strip())
def read_str(): return sys.stdin.readline().strip()
def read_tup(): return map(int, sys.stdin.readline().split())
def read_list(): return list(map(int, sys.stdin.readline().split()))

def solve():
    s = read_str()
    res = ''
    for i in range(len(s)-2):
        res += s[i]
    res += 'i'
    print(res)

def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()