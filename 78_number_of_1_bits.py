def hamming_weight(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n = n >> 1
    return res
