def num_jewels_in_stones(jewels: str, stones: str) -> int:
    dic = set(jewels)
    cnt = 0

    for s in stones:
        if s in dic:
            cnt += 1
    
    return cnt