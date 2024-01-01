def reverse_words_3(s: str) -> str:
    words = s.split(' ')
    res = []
    for word in words:
        w = list(word)
        l, r = 0, len(w)-1
        while l <= r:
            w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1

        word = ''.join(w)
        res.append(word)

    return ' '.join(res)    


print(reverse_words_3("Let's take LeetCode contest"))