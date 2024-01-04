def isBadVersion(n: int) -> bool: # this API will be given by Leetcode
    return False

def find_first_bad_version(n: int) -> int:
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        if not isBadVersion(mid):
            l = mid + 1
        else:
            r = mid - 1

    return l
