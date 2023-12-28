def contains_duplicates_set(nums) -> bool:
    return len(nums) != len(set(nums))


print(contains_duplicates_set([1, 2, 3, 1]))


def contains_duplicates_sort(nums) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        print(i)
        if nums[i] == nums[i + 1]:
            return True

    return False


print(contains_duplicates_sort([1, 2, 3, 4]))

