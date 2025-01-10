# https://leetcode.com/problems/walking-robot-simulation/description/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        x, y = 0, 0
        dx = [(0,1), (1,0), (0,-1), (-1,0)]
        index = 0
        dis = 0
        for i in commands:
            if i == -1:
                index = (index + 1) % 4
            if i == -2:
                index = (index + 3) % 4
            else:
                for _ in range(i):
                    nx = x + dx[index][0]
                    ny = y + dx[index][1]

                    if (nx, ny) not in obs:
                        x, y = nx, ny
                        dis = max(dis, x**2 + y**2)
                    else:
                        break
        return dis