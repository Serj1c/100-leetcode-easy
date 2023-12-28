def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True

    l, r = 1, num // 2

    while l <= r:
        mid = (r + l) // 2

        sq = mid * mid
        if sq == num:
            return True

        if sq < num:
            l = mid + 1
        else:
            r = mid - 1

    return False


print(isPerfectSquare(9))
