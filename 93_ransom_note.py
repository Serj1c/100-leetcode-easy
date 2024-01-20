def can_construct(ransomNote: str, magazine: str) -> bool:
    dict_m = {}
    dict_r = {}
    for c in magazine:
        if c in dict_m:
            dict_m[c] += 1
        else:
            dict_m[c] = 1
    
    for c in ransomNote:
        if c in dict_r:
            dict_r[c] += 1
        else:
            dict_r[c] = 1

    for k, v in dict_r.items():
        if k in dict_m:
            if dict_m[k] < v:
                return False
        else:
            return False
    return True


print(can_construct("aa", "aab"))