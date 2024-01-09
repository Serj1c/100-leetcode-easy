def length_of_last_word(s: str) -> int:
    length = 0
    cur = 0
    prev = ''

    for c in s:
        if c == ' ':
            if prev != ' ':
                length = cur
                cur = 0
        else:
            cur += 1

        prev = c
    return length if not cur else cur


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))

def length_of_last_word2(s: str) -> int:
    word = ''
    for i in range(len(s)-1, -1, -1):
        if s[i] == ' ':
            if word:
                return len(word)
        else:
            word += s[i]

    return len(word)

print(length_of_last_word2("Hello World"))
print(length_of_last_word2("   fly me   to   the moon  "))