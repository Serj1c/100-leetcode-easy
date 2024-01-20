def find_disappeared_numbers(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    res = []
    for i in range(1, len(nums)+1):
        if i not in d:
            res.append(i)
    return res


print(find_disappeared_numbers([1,1]))