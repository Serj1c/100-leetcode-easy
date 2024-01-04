def search_insert(nums, target) -> int:
    l, r = 0, len(nums) -1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            if mid == len(nums)-1:
                return mid + 1
            if nums[mid+1] > target:
                return mid + 1
            else:
                l = l + 1
            
        if nums[mid] > target:
            if mid == 0:
                return 0
            if nums[mid-1] < target:
                return mid
            else:
                r = r - 1
            
print(search_insert([1, 3], 2))