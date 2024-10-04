from collections import deque
def solution(bandage, health, attacks):
    t, x, y = bandage
    limit_health = health
    use_index = 0
    n, time = len(attacks), 0
    seq = 0
    while use_index < n:
        if time == attacks[use_index][0]:
            health -= attacks[use_index][1]
            if health <= 0:
                return -1
                
            seq = 0
            time += 1
            use_index += 1
            continue
        
        else:
            health += x
            seq += 1
            time += 1
            if seq == t:
                seq = 0
                health += y
            
            if health > limit_health:
                health = limit_health            
    
    
    return health