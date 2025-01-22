def fibonacci(N):
    # Base condition
    if N <= 1:
        return N

    last = fibonacci(N-1)
    slast = fibonacci(N-2)

    return last + slast

if __name__ == "__main__":
    N = int(input("Enter the number of terms: "))
    print(fibonacci(N))
