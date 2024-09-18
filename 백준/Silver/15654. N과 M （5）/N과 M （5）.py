from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
nums = list(map(int, input().rsplit()))
nums.sort()

output = []
def dfs():
    if len(output) == m:
        print(*output)
        return

    for i in range(n):
        if nums[i] not in output:
            output.append(nums[i])
            dfs()
            output.pop()

dfs()



