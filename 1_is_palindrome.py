def is_palindrome(n: int) -> bool:
    if n < 0:
        return False

    new = 0
    original_n = n

    while n:
        last = n % 10
        n = n // 10

        new = new * 10 + last

    return new == original_n


print(is_palindrome(121))