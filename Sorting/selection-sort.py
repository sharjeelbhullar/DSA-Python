def selection_sort(arr):
    n = len(arr)
    # Selection sort
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        # Swap the found minimum element with the first element
        arr[mini], arr[i] = arr[i], arr[mini]

    print("After selection sort:")
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before selection sort:")
    print(" ".join(map(str, arr)))

    selection_sort(arr)
