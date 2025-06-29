import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))


def find_start(mat):
    for i in range(8):
        for j in range(8):
            if mat[i][j] != '.':
                return (i, j)
            
def solve():
    mat = []
    for _ in range(8):
        mat.append(read_str())
    
    r, c = find_start(mat)
    s = ''
    while r < 8:
        if mat[r][c] != '.':
            s += mat[r][c]
            r += 1
        else:
            break
    
    print(s)


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()