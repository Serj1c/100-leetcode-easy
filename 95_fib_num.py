def fib(n: int) -> int:
    if n < 2:
        return n
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1]+memo[i-2])
    return memo[-1]