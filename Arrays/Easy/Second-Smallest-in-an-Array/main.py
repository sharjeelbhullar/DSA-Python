def secondSmallest(arr):
    n = len(arr)
    if n<2:
        return -1
    small = float('inf')
    secondSmall = float('inf')
    for i in range(n):
        if arr[i] < small:
            secondSmall = small
            small = arr[i]
        elif arr[i] < secondSmall and arr[i] != small:
            secondSmall = arr[i]
    print(small)
    return secondSmall

if __name__ == "__main__":
    arr = [10, 324, 45, 90, 9808]
    print(secondSmallest(arr))

