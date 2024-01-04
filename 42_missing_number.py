def missing_number(nums) -> int:
    nums.sort()

    for i in range(0, len(nums)+1):
        if i < len(nums):
            if i != nums[i]:
                return i
        else:
            return i
        

print(missing_number([9,6,4,2,3,5,7,0,1]))