def find_start(mat):
    for i in range(8):
        for j in range(8):
            if mat[i][j] != '.':
                return (i, j)
            
def solve():
    mat = ['a.......', 'a.......', 'a.......',
        'a.......', 'a.......', 'a.......', 'a.......', 'a.......' ]
    
    r, c = find_start(mat)
    s = ''
    while c < 8:
        if mat[r][c] != '.':
            s += mat[r][c]
            c += 1
        else:
            break
    
    return s

print(solve())