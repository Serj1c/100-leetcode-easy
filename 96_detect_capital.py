def detect_capital_use(word: str) -> bool:
    return word.islower() or word.isupper() or word.istitle()


print(detect_capital_use('USA'))
print(detect_capital_use('USa'))
print(detect_capital_use('Usa'))