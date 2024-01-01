from collections import Counter


def find_difference(s: str, t: str) -> str:
    return list((Counter(t) - Counter(s)))[0]
        

print(find_difference('abcd', 'abcdd'))