def find_length_of_LCIS(nums) -> int:
    res = 0
    cur = 0

    if len(nums) == 1:
        return nums[0]

    for i in range(0, len(nums)):
        if i < len(nums)-1 and nums[i] < nums[i+1]:
            cur += 1
        elif i < len(nums)-1 and nums[i] >= nums[i+1]:
            res = max(cur+1, res)
            cur = 0
        if i == len(nums)-1:
            cur = cur + 1
            res = max(cur, res)
    return res


print(find_length_of_LCIS([1,3,5,4,2,3,4,5]))
print(find_length_of_LCIS([1,3,5,4,7]))
print(find_length_of_LCIS([2,2,2,2,2]))
print(find_length_of_LCIS([1,3,5,7]))

def find_length_of_LCIS2(nums) -> int:
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1]+1
    return max(dp)


print(find_length_of_LCIS([1,3,5,4,2,3,4,5]))
print(find_length_of_LCIS([1,3,5,4,7]))
print(find_length_of_LCIS([2,2,2,2,2]))
print(find_length_of_LCIS([1,3,5,7]))

def find_length_of_LCIS3(nums) -> int:
    res = 1
    cur = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            cur += 1
        else:
            cur = 1
        res = max(cur, res)
    return res


print(find_length_of_LCIS([1,3,5,4,2,3,4,5]))
print(find_length_of_LCIS([1,3,5,4,7]))
print(find_length_of_LCIS([2,2,2,2,2]))
print(find_length_of_LCIS([1,3,5,7]))