def first_uniq_char(s: str) -> int:
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    for i in range(len(s)):
        if dic[s[i]] < 2:
            return i
    return -1
        

print(first_uniq_char('leetcode'))
print(first_uniq_char('loveleetcode'))
print(first_uniq_char('aabb'))