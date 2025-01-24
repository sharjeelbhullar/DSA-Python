# Brute Force Approach
def secondLargest(arr):
    n = len(arr)
    arr.sort()
    largest = arr[n-1]
    secondLargest = -1
    for i in range(n-2, -1, -1):
        if arr[i] != largest:
            secondLargest = arr[i]
            break
    return secondLargest

#Better Approach
def scndLargest(arr):
    n = len(arr)
    largest = arr[0]
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    
    sLargest = -1
    for i in range(n):
        if arr[i] > sLargest and arr[i] != largest:
            sLargest = arr[i]

    return sLargest

# Optimal Approach
def secondLarg(arr):
    n = len(arr)
    if n < 2:
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_large

if __name__ == "__main__":
    arr = [10, 324, 45, 90, 9808]
    print(secondLargest(arr))
    print(scndLargest(arr))
    print(secondLarg(arr))