from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
nums = list(map(int, input().rsplit()))
nums.sort()
output = []
result = []
visited = [False for _ in range(n)]

def dfs():
    if len(output) == m:
        print(*output)
        return

    prev_num = 0
    for i in range(n):
        if visited[i] or prev_num == nums[i]:
            continue

        output.append(nums[i])
        visited[i] = True
        prev_num = nums[i]
        dfs()
        output.pop()
        visited[i] = False

dfs()