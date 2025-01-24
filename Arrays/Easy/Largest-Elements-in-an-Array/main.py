def largest(arr):
    greater = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > greater:
            greater = arr[i]

    return greater

if __name__ == "__main__":
    arr = [10, 324, 45, 90, 9808]
    print(largest(arr))

