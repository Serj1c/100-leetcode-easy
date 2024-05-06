def peak_index_in_mountain_array(arr) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[mid - 1]:
            l = mid
        else:
            r = mid


print(peak_index_in_mountain_array([0, 2, 1, 0]))


def peak_index_in_mountain_array2(arr) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid -1

    return l


print(peak_index_in_mountain_array2([0, 2, 1, 0]))
print(peak_index_in_mountain_array2([0,3,5,12,2]))
