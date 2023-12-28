def my_sqrt(x: int) -> int:
    l, r = 2, x // 2

    while l <= r:
        mid = (l + r) // 2

        sq = mid * mid
        if sq == x:
            return mid

        if sq < x:
            l = mid + 1

        if sq > x:
            r = mid - 1

    return r


print(my_sqrt(8))