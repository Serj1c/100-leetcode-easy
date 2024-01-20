def find_index(haystack: str, needle: str) -> int:
    lh = len(haystack)
    ln = len(needle)

    for i in range(lh - ln+1):
        if haystack[i:i+ln] == needle:
            return i
        
    return -1


print(find_index("sadbutsad", "sad"))
print(find_index("leetcode", "leeto"))
print(find_index("a", "a"))
print(find_index("abc", "c"))