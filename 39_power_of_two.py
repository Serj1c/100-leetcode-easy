def is_power_of_2(n: int) -> bool:
    if n == 1:
        return True
    
    if n < 1:
        return False
    
    return is_power_of_2(n / 2)


print(is_power_of_2(5))