def single_number(nums) -> int:
    ans = 0

    for num in nums:
        ans ^= num

    return ans


print(single_number([1, 2, 2]))