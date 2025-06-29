def solve(n,k,m, nums):
    nums.sort()
    groups = 0
    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        if diff > m:
            diff //= m
            if diff > k:
                groups += 1
            else:
                k -= diff
    return groups

n = 8
k = 2
m = 3
nums = [1, 1, 5, 8, 12, 13, 20, 22]
print(solve(n, k, m, nums))