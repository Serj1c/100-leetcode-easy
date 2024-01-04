def valid_mountain_array(arr) -> bool:
    if len(arr) < 3:
        return False
    
    first_max_i = 0
    second_max_i = len(arr)-1
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1]:
            first_max_i = i
        if arr[i] <= arr[i-1]:
            break

    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            second_max_i = i-1
        if arr[i] >= arr[i-1]:
            break
    if first_max_i == 0:
        return False
    return first_max_i == second_max_i


print(valid_mountain_array([3,5,5]))
print(valid_mountain_array([2, 1]))
print(valid_mountain_array([0, 3, 2, 1]))
print(valid_mountain_array([2, 0, 2]))
print(valid_mountain_array([9,8,7,6,5,4,3,2,1,0]))
print(valid_mountain_array([0,1,2,1,2]))