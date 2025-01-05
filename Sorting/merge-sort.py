def merge(arr, low, mid, high):
    temp = []  # Temporary array
    left = low  # Starting index of the left half of the array
    right = mid + 1  # Starting index of the right half of the array

    # Merging elements into the temporary array in sorted order
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # If there are remaining elements in the left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # If there are remaining elements in the right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copying elements from the temporary array back to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # Sort the left half
    merge_sort(arr, mid + 1, high)  # Sort the right half
    merge(arr, low, mid, high)  # Merge the sorted halves


if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    print("Before Sorting Array:")
    print(" ".join(map(str, arr)))

    merge_sort(arr, 0, len(arr) - 1)

    print("After Sorting Array:")
    print(" ".join(map(str, arr)))
