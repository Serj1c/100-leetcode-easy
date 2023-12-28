def check_if_exist(arr) -> bool:
    seen = set()
    for el in arr:
        if el * 2 in seen or el / 2 in seen:
            return True
        seen.add(el)

    return False


print(check_if_exist([5, 2, 10, 3]))
