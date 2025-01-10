# https://leetcode.com/problems/different-ways-to-add-parentheses/description/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for j in left:
                    for k in right:
                        if expression[i] == '+':
                            res.append(int(j) + int(k))
                        if expression[i] == '-':
                            res.append(int(j) - int(k))
                        if expression[i] == '*':
                            res.append(int(j) * int(k))

        if len(res) == 0:
            res.append(int(expression))
        return res