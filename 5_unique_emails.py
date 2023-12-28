def numUniqueEmails(emails) -> int:
    unique = set()

    for e in emails:
        name, domain = e.split('@')
        name = name.split('+')[0]
        name = name.replace('.', '')

        unique.add(f'{name}@{domain}')

    return len(unique)


print(numUniqueEmails(['ab@b', 'a+b@b', 'a.b@b', 'a@b']))