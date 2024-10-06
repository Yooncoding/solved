def solution(citations):
    answer = 0
    n = len(citations)
    
    citations.sort(reverse=True)
    
    for h in range(n-1):
        # h편의 논문은 h회 이상 인용
        # 나머지 n-h편의 논문은 h회 이하 인용
        print(citations[h], h+1, citations[h+1], h+1)
        if citations[h] >= h+1 and citations[h+1] <= h+1:
            answer = max(answer, h+1)
    
    if citations[-1] >= n-1:
        answer = max(answer, n)
    
        
    return answer