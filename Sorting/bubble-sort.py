def bubble_sort(arr):
    n = len(arr)
    # Bubble sort
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After Using Bubble Sort:")
    print(" ".join(map(str, arr)))

#Optimized
def bubbleSort(arr):
    n = len(arr)
    # Bubble sort
    for i in range(n - 1, -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if not did_swap:
            break

    print("After Using Bubble Sort:")
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort:")
    print(" ".join(map(str, arr)))

    bubble_sort(arr)
    print("\n\nOptimized approach output below:\n")
    bubbleSort(arr)
