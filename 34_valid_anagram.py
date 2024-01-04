def is_valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d = dict()
    for c in s:
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1
    
    for c in t:
        if d.get(c):
            d[c] -= 1
        else:
            return False
        
    return True


print(is_valid_anagram('rat', 'car'))