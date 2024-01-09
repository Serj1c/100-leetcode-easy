def remove_duplicates(nums) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]

    return j + 1


print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))