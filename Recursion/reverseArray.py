def f(i, arr, n):
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    f(i + 1, arr, n)
    
if __name__ == "__main__":
    n = int(input("Enter the length of array: "))
    arr = list(map(int, input("Enter elements of array: ").split()))
    f(0, arr, n)
    print("Reversed Array: ", end=" ")
    print(" ".join(map(str, arr)))

