from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    
    def can_choose(cur_word, next_word):
        diff_cnt = 0
        word_length = len(cur_word)
        for i in range(word_length):
            if cur_word[i] != next_word[i]:
                diff_cnt += 1
        
        return True if diff_cnt == 1 else False
    
    def bfs(begin, target):
        q = deque()
        q.append([begin, 0])
        while len(q):
            cur_word, cnt = q.popleft()
            if cur_word == target:
                return cnt
            
            for i in range(len(words)):
                if can_choose(cur_word, words[i]) and not visited[i]:
                    visited[i] = True
                    q.append([words[i], cnt+1])
        
        return 0
    
    
    answer = bfs(begin, target)
    
    return answer