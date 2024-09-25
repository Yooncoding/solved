from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
nums = list(map(int, input().rsplit()))
nums.sort()
output = []

def dfs(s):
    if len(output) == m:
        print(*output)
        return

    prev_num = 0
    for i in range(s, n):
        if prev_num == nums[i]:
            continue

        output.append(nums[i])
        prev_num = nums[i]
        dfs(i)
        output.pop()


dfs(0)