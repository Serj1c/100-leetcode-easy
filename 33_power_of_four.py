def power_of_four(n: int) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    return power_of_four(n / 4)


print(power_of_four(16), power_of_four(5), power_of_four(1))