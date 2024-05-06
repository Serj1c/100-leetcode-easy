def climb_stairs(n: int) -> int:
    dp = [0] * (n+1)
    if n > 2:
        dp[1], dp[2] = 1, 2
    if n < 3:
        return n

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(45))