import sys
from collections import defaultdict, Counter
from bisect import bisect_right, bisect_left

def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def IS(): return sys.stdin.readline().strip().split()
mod = 998244353


# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

p2 = [1] * 200001
temp = [1] * 200001
check = pow(2, mod - 2, mod)
for i in range(1, 200001):
    p2[i] = (p2[i - 1] * 2) % mod
    temp[i] = (temp[i - 1] * check) % mod

def solve():
    n = I()
    nums = IL()
    count2 = 0
    F = 0
    G = 0
    ans = 0
    for x in nums:
        if x == 3:
            ans = (ans + p2[count2] * F - G) % mod
        if x == 1:
            F = (F + temp[count2]) % mod
            G += 1
        if x == 2:
            count2 += 1
    print(ans)

T = I()
for ___ in range(T):
    solve()