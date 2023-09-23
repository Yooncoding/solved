from sys import stdin

input = stdin.readline

word = input().rstrip()

answer = "z" * len(word)

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        s1 = word[:i][::-1]
        s2 = word[i:j][::-1]
        s3 = word[j:][::-1]
        new_string = s1 + s2 + s3
        answer = min(answer, new_string)

print(answer)