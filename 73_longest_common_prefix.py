def longest_common_prefix(strs) -> str:
    res = ''
    if len(strs) == 0:
        return ''
    first = strs[0]
    for i in range(len(first)):
        flag = True
        for word in strs[1:]:
            if i > len(word)-1 or first[i] != word[i]:
                return res

        res += first[i]
    return res


print(longest_common_prefix(["flower","flow","flight"]))