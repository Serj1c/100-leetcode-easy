def guess(num: int) -> int: # this API will be given by Leetcode
    return 0

def guessNumber(n: int) -> int:
    l, r = 1, n

    while l <= r:
        mid = (l + r) // 2
        if guess(mid) == 0:
            return mid
        
        if guess(mid) == -1:
            r = mid - 1

        if guess(mid) == 1:
            l = mid + 1
