def majority_element(nums) -> int:
    d = dict()
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    most = 0
    el = 0
    for key in d:
        if d[key] > most:
            most = d[key]
            el = key
    return el

print(majority_element([2,2,1,1,1,2,2]))