import sys
import math
import bisect
from collections import Counter, defaultdict

def read_int(): return int(sys.stdin.readline().strip())
def read_str(): return sys.stdin.readline().strip()
def read_tup(): return map(int, sys.stdin.readline().split())
def read_list(): return list(map(int, sys.stdin.readline().split()))

def check(a, b):
    for i in range(len(a) - 1):
        curr, next = a[i], a[i+1]
        if curr > next:
            if b - curr > next:
                return False
            if b - curr <= next:
                a[i] = b-curr
                j = i
                while j > 0:
                    front, back = a[j], a[j-1]
                    if front >= back:
                        break
                    else:
                        if b - back <= front:
                            a[j - 1] = b - back
                            j -= 1
                        else:
                            return False
    return True

def solve():
    n, m = read_tup()
    a = read_list()
    b = read_int()
    
    if check(a, b):
        print('YES')
    else:
        print('NO')


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()